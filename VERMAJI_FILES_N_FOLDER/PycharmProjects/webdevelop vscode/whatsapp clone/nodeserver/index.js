//node server to handle socket.io connections
const io = require('socket.io')(8000, {
  cors: {
    origin: '*',
  },
});

const users = {};

//for new users joining
io.on('connection', (socket) => {
  socket.on('new-user-joined', (name) => {
    users[socket.id] = name;
    socket.broadcast.emit('user-joined', name);
  });

  //when someone sends a new message
  socket.on('send', (message) => {
    socket.broadcast.emit('receive', {
      message: message,
      name: users[socket.id],
    });
  });

  //when someone quits
  socket.on('disconnect', (message) => {
    socket.broadcast.emit('left', users[socket.id]);
    delete users[socket.id];
  });
});
