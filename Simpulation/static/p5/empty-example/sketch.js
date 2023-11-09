function setup() {
  // put setup code here
    createCanvas(400, 400);
}



let direction=1;
let x=200;
let y=200;
let speed=5;
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
	if(x<=moitionX && x<400 && direction==1){
		x=x+speed;
		distance+=1
		if(x==moitionX){
			direction=-1
		}
	} else if(y<=moitionY && y<400 && direction==-1){
		y=y+speed
		distance+=1
		if(y==moitionY){
			direction=1
			moitionX=moitionX-distance
		}
	} else if(x>=moitionX && x>=0 && direction==1){
		x=x-speed
		distance+=1
		if(moitionX==x){
			direction=-1
			moitionY=moitionY-distance
		}
	} else if(y>=moitionY && y>=0 && direction==-1){
		y=y-speed
		distance+=1
		if(y==moitionY){
			direction=1
			moitionX=data[0]+distance
			moitionY=data[1]+distance
		}
	}
	
	
}




