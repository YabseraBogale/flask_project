function newGame(){
    let p1=document.getElementById('p1')
    p1.innerText="0"
    let p2=document.getElementById('p2')
    p2.innerText="0"
}

function roll_player1(){
    let num=Math.floor(Math.random()*(7-1)+1)
    let rolled=document.getElementById('rolled')
    rolled.innerText=num.toString()
    let p1_price=Number(document.getElementById('p1').innerText)
    if (num!=1){
        let p1=document.getElementById('p1')
        p1.innerText=(p1_price+num).toString()
    } else if(p1_price==100){
        p1.innerText="You Win"
    }
    else{
        let p1=document.getElementById('p1')
        p1.innerText="0"
        let btn1=document.getElementById("btn1")
        let btn2=document.getElementById("btn2")
        btn2.disabled=false
        btn1.disabled=true
        document.getElementById("turn").innerText="player 2"
    }
}

function hold_player(){
    let turn =document.getElementById("turn").innerText
    if (turn == "player 1"){
        let btn1=document.getElementById("btn1")
        let btn2=document.getElementById("btn2")
        btn2.disabled=false
        btn1.disabled=true
        document.getElementById("turn").innerText="player 2"
    }
    else{
        let btn1=document.getElementById("btn1")
        let btn2=document.getElementById("btn2")
        btn2.disabled=true
        btn1.disabled=false
        document.getElementById("turn").innerText="player 1"
    }

}

function roll_player2(){
    let num=Math.floor(Math.random()*(7-1)+1)
    let rolled=document.getElementById('rolled')
    rolled.innerText=num.toString()
    let p2_price=Number(document.getElementById('p2').innerText)
    if (num!=1){
        let p2=document.getElementById('p2')
        p2.innerText=(p2_price+num).toString()
    } else if(p2_price==100){
        p2.innerText="You Win"
    }
    else{
        let p2=document.getElementById('p2')
        p2.innerText="0"
        let btn1=document.getElementById("btn1")
        let btn2=document.getElementById("btn2")
        btn2.disabled=true
        btn1.disabled=false
        document.getElementById("turn").innerText="player 1"
    }
}