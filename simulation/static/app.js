let robot=document.querySelector(".robot")
let env=document.querySelector(".env")
let y=0
let speed=6
let direction=1
setInterval(function(){
	y = y + speed * direction;
      if (y >= env.innerHeight/3 - 50) {
         direction = -1;
      }
      if (y <= 0) {
         direction = 1;
      }
      robot.style.top = y + '%';
	


},1000);
