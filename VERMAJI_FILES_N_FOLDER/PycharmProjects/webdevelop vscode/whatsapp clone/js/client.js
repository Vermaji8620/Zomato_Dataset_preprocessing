import { io } from 'socket.io-client'
const socket = io('https://localhost:8000');

//get dom elements in a js variables
const form = document.getElementById('send-container');
const messageinput = document.getElementById('messageinp');
const messagecontainer = document.querySelector('.container');
var audio = new Audio('order-99518.mp3');

//function that will append event to the container
const append = (message, position) => {
  const messageelement = document.createElement('div');
  messageelement.innerText = message;
  messageelement.classList.add(message);
  messageelement.classList.add(position);
  messagecontainer.append(messageelement);
  if (position == 'left') {
    audio.play();
  }
}

//ask the new user for his/her name and let the server know
const name = prompt("enter your name to join");
socket.emit('new-user-joined', name);

//if a new user joins then receive the event from the server
socket.on('user-joined', (name) => {
  append(`${name} joined the chat`, 'right');
});

//if the server sends a message then receive it
socket.on('receive', (data) => {
  append(`${data.message}:${data.user}`, 'left');
});

//if  a user leaves the chat. then append the info to the container
socket.on('left', (name) => {
  append(`${name} left the chat`, 'left');
});

//if the form gets submitted then send the message to the server
form.addEventListener('submit', (e) => {
  const message = messageinput.value;
  append(`You: ${message}`, 'right');
  socket.emit('send', message);
  e.preventDefault();
  messageinput.value = "";
});