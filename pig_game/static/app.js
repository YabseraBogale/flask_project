function newGame(){
    location.reload();
}
function roll_player1(){
    let num=Math.floor(Math.random()*(7-1)+1)
    let added=Math.floor(Math.random()*(100-1)+1)
    let rolled=document.getElementById('rolled')
    rolled.innerText=num.toString()
    let p1_price=Number(document.getElementById('p1').innerText)
    if (p1_price>=100){
        p1.innerText="You Win"
        let btn1=document.getElementById("btn1")
        let btn2=document.getElementById("btn2")
        btn1.disabled=true
        btn2.disabled=true
    } else if(num!=1 && p1_price<100){
        let p1=document.getElementById('p1')
        if (p1_price+added>=100){
            p1.innerText=(p1_price+added).toString()+ " You Win"
            let btn1=document.getElementById("btn1")
            let btn2=document.getElementById("btn2")
            btn2.disabled=true
            btn1.disabled=true
        } else{
            p1.innerText=(p1_price+added).toString()
        }
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
    let added=Math.floor(Math.random()*(100-1)+1)
    let rolled=document.getElementById('rolled')
    rolled.innerText=num.toString()
    let p2_price=Number(document.getElementById('p2').innerText)
    if (p2_price>=100){
        console.log(p2.innerText);
        p2.innerText="You Win"
        let btn1=document.getElementById("btn1")
        let btn2=document.getElementById("btn2")
        btn1.disabled=true
        btn2.disabled=true

    } else if(num!=1 && p2_price<100){
        let p2=document.getElementById('p2')
        if (p2_price+added>=100){
            p2.innerText=(p2_price+added).toString()+ " You Win"
            let btn1=document.getElementById("btn1")
            let btn2=document.getElementById("btn2")
            btn2.disabled=true
            btn1.disabled=true
            
        } else{
            p2.innerText=(p2_price+added).toString()
        }
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