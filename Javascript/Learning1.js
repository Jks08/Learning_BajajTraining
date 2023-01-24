const fruits = ['apple', 'banana', 'orange', 'pineapple', 'mango', 'grapes'];
console.log(fruits.toString())
console.log(fruits.join(' * '))
console.log(fruits.pop())
console.log(fruits.push('kiwi'))
console.log(fruits.shift())
console.log(fruits.unshift('grapes'))
fruits[fruits.length] = 'durian'
console.log(fruits)
delete fruits[0]
delete fruits
const flowers=['rose', 'jasmine', 'lily', 'lotus']
const fruits1 = ['apple', 'banana', 'orange', 'pineapple', 'mango', 'grapes'];
const flowers_fruits = fruits1.concat(flowers)
console.log(flowers_fruits)
fruits2 = ['apple', 'banana', 'orange', 'pineapple', 'mango', 'grapes'];
console.log(fruits2.splice(1, 4,'banana','grapes'))
console.log(fruits2)


class Cars{
    constructor(name,year){ //constructor is like self, but can't change the name
        this.name=name;
        this.year=year;
    }
    age(){ //not necessary to use function keyword before the function name
        let date = new Date();
        return date.getFullYear() - this.year;
    }
}

let myCar = new Cars("Ford", 2014);
console.log("My car is " + myCar.age() + " years old");