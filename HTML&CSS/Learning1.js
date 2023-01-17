/*function startListen(){ * }
document.getElementsById('demo').addEventListener('click',myFunction)
function myFunction() 
{

    const numbers1 = [45, 4, 9, 16, 25,-30];
    //const numbers2 = numbers1.map(myFunction);
    let suii=0;
    for (let i = 0; i < numbers1.length; i++) {
        suii += numbers1[i];
        
    }
    document.getElementById('demo').innerHTML=suii;
}
//document.getElementById('demo').innerHTML = myFunction();*/

window.onload=function(){
    var buttonElement = document.getElementById("demo");
    if (buttonElement){
        buttonElement.addEventListener('click',myFunction);
    }

    function myFunction(){
        const numbers1=[45,4,9,16,25,-30];
        let suii=0;
        for(let i=0;i<numbers1.length;i++){
            suii+=numbers1[i];
        }
        buttonElement.innerHTML=suii;
    }
}
window.onclick=function(){
    var buttonElement1 = document.getElementById('changeColor');
    if(buttonElement1){
        buttonElement1.addEventListener('click',myFun());
    }
    
    function myFun(){
        var randCol="";
        var alChar="0123456789ABCDEF";
        var idx = 10

        for(var i=0; i<6; i++){
            randCol += alChar[Math.floor(Math.random()*16)];
        }

        // console.log(randCol);
        document.body.style.backgroundColor= "#"+randCol;
    }
}

setInterval(
    function () {
        var randomColor = Math.floor(Math.random()*16999215).toString(16);
        document.body.style.backgroundColor = "#"+randomColor;
    },2000);