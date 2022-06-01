show dbs
show harrykart
show collections

db.items.find()
db.items.updateOne({name:"samsung"}, {$set:{price:2}})
db.items.find()
db.items.updateMany({name:"samsung"}, {$set: {price:3, rating:1}})