let character=document.getElementById("character")
let interval
let both=0

function moveLeft(){
    let left=parseInt(window.getComputedStyle(character).getPropertyValue("left"))
    if(left<380){
        character.style.left=(left+2+Math.random())+"px"
    }else{
        character.style.left=left
    }
}
function moveRight(){
    let left=parseInt(window.getComputedStyle(character).getPropertyValue("left"))
    if(left>0){
    character.style.left=(left-2+Math.random())+"px"
    }else{
        character.style.left=left
    }
}
function moveUp(){
    let top=parseInt(window.getComputedStyle(character).getPropertyValue("top"))
    if(top<480){
    character.style.top=(top+2+Math.random())+"px"}
}
function moveDown(){
    let top=parseInt(window.getComputedStyle(character).getPropertyValue("top"))
    if(top>0){
    character.style.top=(top-2+Math.random())+"px"}
}
document.addEventListener("keydown", event=>{
    if(both==0){
        both++
        if(event.key==="ArrowLeft"){
            interval=setInterval(moveLeft,1)
        }
        if(event.key==="ArrowRight"){
            interval=setInterval(moveRight,1)
        }
        if(event.key==="ArrowUp"){
            interval=setInterval(moveUp,1)
        }
        if(event.key==="ArrowDown"){
            interval=setInterval(moveDown,1)
        }
    }
})
document.addEventListener("keyup",event=>{
    clearInterval(interval)
    both=0
})
