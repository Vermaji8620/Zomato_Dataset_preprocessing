show dbs
use harrykart
show collections
db.items.find({price:2000})

//deleting items from the mongodb database 
db.items.deleteOne({price:20000})
db.items.deleteMany({price:20000})
