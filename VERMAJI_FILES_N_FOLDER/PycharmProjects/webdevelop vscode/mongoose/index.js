//mongoose ek tarah ka layer hai jo ki node.js ko mongo k sath me connect krne me help krta hai...
const mongoose = require("mongoose");//starting the mongoose

main().catch((err) => console.log(err));

async function main() {
  await mongoose.connect("mongodb://localhost:27017/harrykart");
  console.log("mongoose is connected");
}

//schema banaya (matlb ki kon sa chiz kis tarah se rhega database k andar uska ek schema banaya gya hai, sidha sidha ek tarah ka orientation bol skte hai ki kiske baad kya aayega)
const kittySchema = new mongoose.Schema({
  name: String,
});

// NOTE: methods must be added to the schema before compiling it with mongoose.model()
kittySchema.methods.speak = function speak() {
  const greeting = "My name is " + this.name;
  console.log(greeting);
};

//model banaya
const Kitten1 = mongoose.model("harrykitty", kittySchema);//ye schema ka ek tarah ka model banaya jata hai, taki jo schema ko ek tarah se bol skte hai, ki lock kra ja sake
const Kitten2 = mongoose.model("harrykitty", kittySchema);//background me automatic harrykitty ka harrykitties database ban jata hai, aur uske andar sb kch save ho jata hai.

//object banaya
const harrykitty1 = new Kitten1({ name: "harrykitty1 name" });
console.log(harrykitty1.name); //
harrykitty1.speak();

const harrykitty2 = new Kitten2({ name: "harrykitty2 name" });
console.log(harrykitty2.name); //
harrykitty2.speak();

harrykitty1.save();
// harrykitty1.speak();

harrykitty2.save();
// harrykitty2.speak();

Kitten1.find();
Kitten2.find();



// harrykitty1 = await harrykitty1.find();
// console.log(harrykitty1);

// harrykitty2 = await harrykitty2.find();
// console.log(harrykitty2);
// await Kitten.find({ name: /^harrykitty/ });