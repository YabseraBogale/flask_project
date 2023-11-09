function setup() {
  // put setup code here
    createCanvas(400, 400);
}



let direction=1;
let x=200;
let y=200;
let speed=1;
let distance=1
let moitionX=220;
let moitionY=220;

function draw() {
  // put drawing code here
  	background(220);
	circle(x, y, 20);
	//console.log("moitionX",moitionX,"x",x,"direction",direction);
	if(x<moitionX && direction==1){
		x=x+1
		distance+=1
		if(x==moitionX){
			direction=-1
		}
	} else if(y<moitionY && direction==-1){
		y=y+1
		distance+=1;
		if(y==moitionY && moitionX==x){
			direction==1
			moitionX=moitionX+distance
		}
	} else if(x>moitionX && direction==1){
		x=x-1;
		distance+=1
		if(x==moitionX){
			direction=-1
			moitionY=moitionY-distance
		}
	} else if(y>moitionY && direction==-1){
		y=y-1
		distance==1
		if(y==moitionY){
			direction=1
			moitionX=moitionX+distance
		}
	}
	
	
	
	
}




