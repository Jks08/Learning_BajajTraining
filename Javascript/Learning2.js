// block scope, function scope, global scope

// Blockscope

m=4
n=2
if(m>n){
    var p =4;
}
console.log(p) //accessible outside the block

if(m>n){
    let q =4;
    console.log(q) //accessible inside the block
}

console.log(q) //not accessible outside the block

if(m>n){
    const r =4;
}

console.log(r) //not accessible outside the block

// Function scope

function f1(){ let v1=9;}
function f2(){ var v2=10;}
function f3(){ const v3=11;}

console.log(v1,v2,v3) //not accessible outside the function. can be accessed only inside the function

// Global scope

var v5=69;
var v6=71;
var v7 = 80;

function check(){
    v5=69;
    v7=89;
}
console.log(v5,v6,v7) //accessible outside the function as well as inside the function as it is global scope.