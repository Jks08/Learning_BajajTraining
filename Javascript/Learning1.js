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

class Emp{
    static company = "Bajaj Markets"; //static variable and these must be static. static can be called by class name.
    constructor(eid,ename,esal){
        this.eid=eid;
        this.ename=ename;
        this.esal=esal;
    }
    set emp_id(eid){this.eid=eid;}
    set emp_name(ename){this.ename=ename;}
    set emp_sal(esal){this.esal=esal;}
    get emp_id(){return this.eid;}
    get emp_name(){return this.ename;}
    get emp_sal(){return this.esal;}

    disp(){
        console.log("Employee ID: "+this.eid);
        console.log("Employee Name: "+this.ename);
        console.log("Employee Salary: "+this.esal);
    }

    static get_company(){
        return Emp.company;
    }
}

let e1 = new Emp("E001","John Doe",60000);
console.log(e1.disp(),Emp.get_company());
console.log(e1.eid,e1.ename,e1.esal);
e1.eid="E002";
e1.ename="Jane Doe";
e1.esal=70000;
console.log(e1.eid,e1.ename,e1.esal);
Emp.company = "Bajaj Markets Pvt. Ltd.";
console.log(Emp.get_company());

class Meetup{
    constructor(organizer){
        this.organizer = organizer;
    }
}

class TeachMeet extends Meetup{
    constructor(organizer,topic){
        super(organizer);
        this.topic = topic;
    }
}

let tm = new TeachMeet("John Doe","Javascript");
console.log(tm.organizer,tm.topic);