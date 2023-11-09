function setup() {
  // put setup code here
    createCanvas(400, 400);
}



let movingObject=[200,200,205,205,1]

function draw() {
  // put drawing code here
	background(220);
	
	// movingObject=[Initail_Point_X,Initail_Point_Y,Step_X,Step_Y,direction]
	circle(movingObject[0], movingObject[1], 20);
	//console.log(movingObject[0]);
	Motion(movingObject,5);

}

function Motion(movingObject,speed){
		movingObject[2]=movingObject[0]+speed
		movingObject[3]=movingObject[1]+speed
		switch(movingObject){
			case movingObject[0]<=movingObject[2] && movingObject[1]<=movingObject[3]  && movingObject[4]==1:
				movingObject[0]=movingObject[0]+speed
				console.log(movingObject[0]);
				if(movingObject[0]==movingObject[2]){
					movingObject[4]=-1
				}
			case movingObject[0]==movingObject[2] && movingObject[1]<=movingObject[3]  && movingObject[4]==-1:
				movingObject[1]=movingObject[1]+speed
				if(movingObject[1]==movingObject[3]){
					movingObject[4]=1
					movingObject[0]=movingObject[0]+movingObject[2]
				}
			
		}
		
}
