//inserting data in mongodb 

use harrykart
db.items.insertOne({name:"samsung", price:22000, rating:4.5, sold:98})
db.items.insertMany({name:"samsung", price:22000, rating:4.5, sold:98})

