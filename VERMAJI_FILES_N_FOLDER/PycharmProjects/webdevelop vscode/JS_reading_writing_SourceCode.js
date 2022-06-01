const fs=require("fs")

//reading of a file
const text=fs.readFileSync("(2)self_designed_website.html", "utf-8")
console.log("the content of the file is")
console.log(text)
console.log("this is the end")

//writing in a file
fs.writeFileSync('test.txt', text)
//new flle is created and text is written in there
