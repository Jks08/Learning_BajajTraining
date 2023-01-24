const ages = [12, 14, 16, 18, 20, 22, 24, 26, 28, 30];
function checkAge(age){
    if(age >= 18){
        return true;
    }
    return false;
}
function myFunction(){
    // console.log(ages.find(checkAge));
    var leese = Array();
    for (let i = 0; i < ages.length; i++) {
        if(checkAge(ages[i])){
            leese.push(ages[i]);
        }
    }
    document.getElementById("demo1").innerHTML = leese;
}
myFunction();

// find() -> returns the value of the first element in the array that satisfies the provided testing function. Otherwise undefined is returned.