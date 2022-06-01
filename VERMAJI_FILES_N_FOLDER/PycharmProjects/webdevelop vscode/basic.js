//STEPS KI KAISE KRNA HAI
// 1. NODE.JS KA OFFICIAL WEBSITE PE JAKE ABOUT SECTION ME JAKE WAHA PE KA CODE COPY KRKE YAHA PE AKE CODE PASTE KR DENA HAI ..USKE BAAD ME 'plain' word ko 'html' me change kr dena hai....phir niche wala res.end me ake uske andr k chij delete krke usme wo chij paste kr dena hai....normal go live pe click krke webpage khulega...jisme html, css rhega, ab backend kholne k liye terminal me jake new terminal kholke....waha pe--  node.(filename->tab) aur phir enter....aur wo server ko load kr skte hai...


const http = require('http');

const hostname = '127.0.0.1';
const port = 3000;

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/html');
  res.end(`<!DOCTYPE html>
  <html lang="en">
  
  <head>
      <meta charset="UTF-8">
      <meta http-equiv="X-UA-Compatible" content="IE=edge">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>webdesign practicing</title>
      <style>
          body {
              background-color: black;
          }
  
          .conta {
              width: 15px;
              height: 20px;
              position: relative;
              left: 180px;
              background-color: white;
          }
  
  
          #box1 {
              width: 900px;
              height: 36px;
              background-color: rgb(229, 155, 19);
              color: white;
              font-size: 25px;
              display: flex;
              border: 6px solid white;
              border-bottom: 100px solid white;
          }
  
          #box1 .p {
              font-weight: bold;
              margin: 2px 80px;
          }
  
          #box2 {
              width: 900px;
              height: 480px;
              background: url(girl.jpg);
              background-size: 100%;
              color: white;
              margin: -3px 0px;
              padding: 9px 0px;
              opacity: .9;
              border: 6px solid white;
          }
  
          #box2 .q {
              font-size: 4rem;
              position: relative;
              top: 4rem;
              font-family: Andalus;
              left: 16rem;
  
          }
  
          #box2 .r {
              position: relative;
              top: 3rem;
              left: 20rem;
              font-size: 1.5rem;
          }
  
          #box2 .s {
              position: relative;
              left: 10rem;
              top: 5rem;
          }
  
          .inside {
              width: 130px;
              height: 30px;
              background-color: orange;
              color: white;
              position: relative;
              bottom: 32px;
              left: 440px;
              border-radius: 5px;
          }
  
          .instxt {
              position: relative;
              bottom: 3px;
              left: 30px;
              font-size: 25px;
          }
  
          .oneclass {
              display: flex;
              margin: 74px 115px;
              padding: 10px 14px;
          }
          
          /* .boxing::before{
              position: relative;
              z-index: -1;
          } */
          
          .boxing {
              color: rgb(247, 247, 247);
              margin: 2px 2px;
              padding: 2px 2px;
              background: url(backgrnd.jpg);
              opacity: 0.6;
              font-weight: bold;
              font-style: italic;
  
          }
  
          
          .boxing1 {
              color: white;
              background-color: orange;
              margin: 2px 37px;
              padding: 2px 14px;
          }
  
          #written {
              margin: 2px 150px;
              padding: 2px 2px;
          }
      </style>
  </head>
  
  <body>
      <div class="conta">
          <div id="box1">
              <div class="p">
                  Chegg
              </div>
          </div>
          <div id="box2">
              <div class="q">
                  The Student Hub
              </div>
              <div class="r">
                  Save up to 90% on textbooks
              </div>
              <div class="s">
                  <input type="text" style="width: 570px; height: 30px;"
                      placeholder="Enter ISBN, title, or author's name">
                  <div class="inside">
                      <div class="instxt">
                          <input type="button" value="Find Book">
                      </div>
                  </div>
              </div>
              <div class="oneclass">
                  <div class="boxing">
                      SELL BOOKS
                  </div>
                  <div class="boxing">
                      NEW EXPLORE CAREERS
                  </div>
                  <div class="boxing1">
                      24/7 STUDY HELP
                  </div>
                  <div class="boxing">
                      RETURN BOOKS
                  </div>
                  <div class="boxing">
                      FIND INTERNSHIPS
                  </div>
              </div>
              <div id="written">
                  "Hate to wait? Courtesy Textbook when available while your books are on the way."
              </div>
          </div>
      </div>
  </body>
  
  </html>`);
});

server.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});