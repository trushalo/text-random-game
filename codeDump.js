//Functions





function randomIntFromInterval(min, max) { // min and max included 
  return Math.floor(Math.random() * (max - min + 1) + min);
}

//Starting variable sets

var page=1;

//buttons
var b1=document.getElementById("b1");
var b2=document.getElementById("b2");
var b3=document.getElementById("b3");
var b4=document.getElementById("b4");

/*function b1test ()
{b1='you clicked it!'}


b1.on('click',(b1) => {
  b1='you clicked it'
  
})
*/


//characters
class Character 
{
  constructor (name, strength, weakness, loss, id, count) {
    this.name = name,
    this.strength = strength,
    this.weakness = weakness,
    this.loss = loss,
    this.id = id,
    this.count =count;
}
};
var bob = new Character ('Bob','engine','combat','reckless',0,1);

var dave = new Character ('Dave','guns','law', 'raid', 1,0);

var chicken = new Character ('Shelly', 'surreal', 'diplomacy','hunger', 2,0);

var coriolas = new Character ('Coriolas', 'diplomacy', 'reckless','lie',3,1);

var EmptyChar = [bob,dave,chicken,coriolas];
//Ship this error
/*
class Ship
{
constructor (speed, nav, scan, legal, cargo, mass)
this.speed=speed,
this.nav=nav,
this.scan=scan,
this.legal=legal,
this.cargo=cargo,
this.mass=mass;
}
*/

//First page text options
var shipone = ['You wake with sandpaper marinated in rotten guava swirling filling your mouth. You lie slanted on a dirty mattress crushed between a steering console decorated in exposed wires and a cheap tin wall that wafts with the familiar smell of a broken head. This is  your ship.','You jam a fork wrapped in copper wire between the main processor and the navigation console and are pleasantly surprised to see the console security disarm without any alarms going off. The ship is now yours.','Ship with no engine.'];

var firstchoice = 
[
 'It might be a little rough around the edges but if it actually had an engine installed you could outfly anything!',
 'b',
 'c',
 'd'
  ]

 var secondchoice = ['A sapient chicken. Fine, it is just a normal chicken. Space gets lonely, okay!',
'A highly illegal Artificial Intelligence unironically named Dave.',
'Your annoying younger sibling who is constantly gushing about the "roaming the system."',
'A drunk who you pulled off the floor at a local spaceport bar.'];

//b1.addEventListener("click")

//Page 1 run
if (page = 1)
{
  document.getElementById("b1").innerHTML = firstchoice[0];
document.getElementById("b2").innerHTML=firstchoice[1];
document.getElementById("b3").innerHTML = firstchoice[2];
document.getElementById("b4").innerHTML=firstchoice[3];
let e1 = document.getElementById("eventtxt").innerHTML = shipone[randomIntFromInterval(0, shipone.length)];

}

console.log(
document.getElementById("b1").innerHTML)
//Page 2 run

function b1click()
{
  return document.getElementById("b1").innerHTML;
  advance();
}

function b2click()
{
  return document.getElementById("b2").innerHTML;
  advance();
}

function b3click()
{
  return document.getElementById("b3").innerHTML;
  advance();
}

function b4click()
{
  return document.getElementById("b4").innerHTML;
  advance();
}

function advance()
{
  page++;
  if (page=2)
  {
  document.getElementById("b1").innerHTML = secondchoice[0];
document.getElementById("b2").innerHTML=secondchoice[1];
document.getElementById("b3").innerHTML = secondchoice[2];
document.getElementById("b4").innerHTML=secondchoice[3];
document.getElementById("eventtxt2").innerHTML = shipone[randomIntFromInterval(0, shipone.length)];
    
  }
};

//class Event 



//console.log(EmptyChar[3])
/*Create an object called shape that has the type property and a getType() method.
Define a Triangle() constructor function whose prototype is shape. Objects created with Triangle() should have three own properties—a, b, and c, representing the lengths of the sides of a triangle.

Add a new method to the prototype called getPerimeter().
*/
