function setup() {
  // put setup code here
    createCanvas(400, 400);
}



let direction=1;
let x=200;
let y=200;
let speed=1;
let distance=1
let moitionX=x+10;
let moitionY=y+10;
const data=[moitionX,moitionY]
function draw() {
  // put drawing code here
	background(220);
	let Data={"distance":distance,"moitionX":moitionX,"moitionY":moitionY}
	circle(x, y, 20);
	console.log(Data);
	
	
	
}




