//for searching the data in mongodb
use harrykart
//this query will return all the objects with rating equal to 3.5
db.items.find({"rating":6.5})
db.items.find({"rating":{$gt: 3.5}})//for filtering the objects having rating greater than 3.5
db.items.find({"rating":{$gte: 3.5}})//for filtering the objects having rating greater than or equal to 3.5
db.items.find({"rating":{$gte: 3.5}, "roll":{$gt:50}})//for filtering the objects having rating greater than or equal to 3.5
db.items.find({$or:[{roll:{$lt:1000}}, {price:{$gt:114000}}]})//the first object can be ececuted or the second object can be executed