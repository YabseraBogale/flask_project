
setInterval(function(){
	let ele=document.querySelector(".robot")
	let position= ele.getBoundingClientRect()
	console.log(position);
	//ele.style=`margin-left:${position.x-5}px;`
	if(position.x<position.right){
		ele.style=`margin-left:${position.left/2+0.5}px;`
	}
	else{
		ele.style=`margin-left:${position.left/2-0.5}px;`
	}

},1000);
