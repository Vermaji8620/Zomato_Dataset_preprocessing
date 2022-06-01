const http=require('http')
const fs=require('fs')
const fileContent=fs.readFileSync('(2)self_designed_website.html')
const server=http.createServer((req, res)=>{
    res.writeHead(200, {'Content-type':'text/html'})
    res.end(fileContent)
})

server.listen(8000, '127.0.0.1', ()=>{
    console.log("listening on port 8000")
})
//80 porting is the default....agar 80 dete hai, to, browser me sirf url dene se hi kaam ban jayega, port dene ka koi jarurat nai hai, lekin agr 80 nai deke kch aur diya to browser me url k sath sath port v dena hoga 
