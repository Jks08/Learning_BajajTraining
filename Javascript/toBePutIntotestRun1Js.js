// window.onclick=function(){
//     var buttomElement1 = document.getElementById('demo');
//     if(buttomElement1){
//         buttomElement1.addEventListener('click',myCalculator);
//     }

//     function myCalculator(){
//         var x = prompt("Enter a number");
//         var y = prompt("Enter another number");
//         var z = prompt("Enter the operation to perform");
//         var res;
//         if (z == "+"){
//             res = parseInt(x) + parseInt(y);
//         }
//         else if (z == "-"){
//             res = parseInt(x) - parseInt(y);
//         }
//         else if (z == "*"){
//             res = parseInt(x) * parseInt(y);
//         }
//         else if (z == "/"){
//             res = parseInt(x) / parseInt(y);
//         }
//         else{
//             res = "Invalid Operation";
//         }
//         document.getElementById("demo").innerHTML = "The result is " + res;
//     }
// }

function myCalculator(){
    var x = prompt("Enter a number");
    var z = prompt("Enter the operation to perform");
    var y = prompt("Enter another number");
    var res;
    
    if (z == "+"){
        res = parseInt(x) + parseInt(y);
    }
    else if (z == "-"){
        res = parseInt(x) - parseInt(y);
    }
    else if (z == "*"){
        res = parseInt(x) * parseInt(y);
    }
    else if (z == "/"){
        res = parseInt(x) / parseInt(y);
    }
    else if(z=='^'){
        res = parseInt(x) ** parseInt(y);
    }
    else{
        res = "Invalid Operation";
    }
    document.getElementById("demo").innerHTML = "The result is " + res;
}
