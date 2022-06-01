// synchronous or blocking
// -line by line execution
// asynchronous or non-blocking
// -line by line execution not guranteed
const fs=require("fs")
fs.readFile("(2)self_designed_website.html", "utf-8", (a,b)=>{
    console.log(a,b)
})
console.log("this is a message")//yeh wala sytax ka output pehle a jayega....matlab ki iske jo pehle wala syntax hai wo jb tk read krega, tab tk thode nah program ruka hua rhega, program to aage badhte rhega ,,,,isiliye run hote hote last wala syntax ka output pehle print ho jata hai, bhale hi ye baad me likaha hua hai

//yeh non-synchronous mode me program likhe hai..matlb ki jo execute ho rha h usko execute kr do,...bhale hi serialwise syntax me kahi pe v likha hua ho...taki program running k time pe bada file read krne k chalte baki k execution me deri na lage

