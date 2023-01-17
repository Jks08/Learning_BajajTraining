const numbers1 = [45, 4, 9, 16, 25];
const numbers2 = numbers1.map(myFunction);

document.getElementById('demo').innerHTML = numbers2
function myFunction(value) 
{
    return value * 2;
}