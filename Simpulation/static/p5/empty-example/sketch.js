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
  	fill(0,22,0);
	circle(x, y, 20);
	if(x<=moitionX && x<400 && x>0 && direction==1){
		x+=1
		distance+=1
		if(x==moitionX){
			direction=-1
		}
	} else if(y<=moitionY && y<400 && y>0 && direction==-1){
		y+=1
		distance+=1
		if(y==moitionY){
			direction=1
		}
	} else if(x>=moitionX && x<400 && x>0 && direction==1){
		x-=1
		distance+=1
		if(moitionX==x && 0<moitionX-distance){
			moitionX=moitionX-distance
		} else if(moitionX==x && 0>moitionX-distance){
			moitionX=distance-moitionX
		}
	} else if(y>=moitionY && y<400 && y>0 && direction==1){
		y-=1
		distance+=1
		if(moitionX==x && 0<moitionY-distance){
			moitionX=moitionX-distance
		} else if(moitionY==y && 0>moitionY-distance){
			moitionY=distance-moitionY
		}
	
	}
	
	
}




