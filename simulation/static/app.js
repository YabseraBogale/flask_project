
setInterval(function(){
	let ele=document.querySelector(".robot")
	let position= ele.getBoundingClientRect()
	console.log(position);
	//ele.style=`margin-left:${position.x-5}px;`
	if(position.x>0){
		
	}

},1000);
