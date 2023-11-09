function setup() {
  // put setup code here
    createCanvas(400, 400);
}



function draw() {
  // put drawing code here
	background(220);
	
	// movingObject=[Initail_Point_X,Initail_Point_Y,Step_X,Step_Y,direction]
	let movingObject=[200,200,5,5,1]
	circle(movingObject[0], movingObject[1], 20);
	Motion(movingObject,6);

}

function Motion(movingObject,speed){
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
			case movingObject[0]>=movingObject[2] && movingObject[1]==movingObject[3]  && movingObject[4]==1:
				movingObject[0]=movingObject[0]-speed
				if(movingObject[0]==movingObject[2]){
					movingObject[4]=-1
					movingObject[1]=movingObject[1]+movingObject[3]
					
				}
			case movingObject[0]==movingObject[2] && movingObject[1]>=movingObject[3]  && movingObject[4]==-1:
				movingObject[1]=movingObject[1]-speed
				if(movingObject[1]==movingObject[3]){
					movingObject[4]=1
				}
		}
		
}
