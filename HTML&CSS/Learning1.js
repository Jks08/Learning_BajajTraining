function myFunction() 
{
    const numbers1 = [45, 4, 9, 16, 25,-30];
    //const numbers2 = numbers1.map(myFunction);
    let suii=0;
    for (let i = 0; i < numbers1.length; i++) {
        suii += numbers1[i];
        
    }
    return suii;
}
document.getElementById('demo').innerHTML = myFunction();