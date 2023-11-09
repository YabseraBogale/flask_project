function setup() {
  // put setup code here
    createCanvas(400, 400);
}

function moitionMove(pointX,pointY){
	return [pointX+10,pointY+10]
}


let direction=1
let x=200
let y=200
let moition=moitionMove(x,y)
function draw() {
  // put drawing code here
	background(220);
	circle(x, y, 20);
	moveRobot(x,y,direction,moition);
	
}


function moveRobot(pointX,pointY,direction,speed,movement){
	switch(arr){
		case pointX<=movement[0] && pointX<400 && direction==1:
			pointX=pointX+speed
			if(pointX==movement[0]){
				direction=-1
			}
		case pointY<=movement[1] && pointY<400 && direction==-1:
			pointy=pointY+speed
			if(pointY==movement[1]){
				direction=1
			}
	}
	
}

