function setup() {
  // put setup code here
    createCanvas(400, 400);
	background(0,20,0);

}



let direction=1;
let x=0;
let y=0;
let speed=1;
let distance=1
let moitionX=220;
let moitionY=220;

function draw() {
  // put drawing code here


	noStroke(220);
	fill(220);
	circle(x, y, 20);
	console.log(x,y);
	if(x>=0 && x<400 && direction==1){
		x+=10
		if(x==400){
			direction=-1
			y+=10
		}
	} else if(x>0  && direction==-1){
		x-=10
		if(x==0){
			y+=10
			direction=1
			if(y>420){
				alert("Simulation Over")
				noLoop();
			}
		}
	}
}




