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

