function Car(brand, speed, fuel) {
    this.brand = brand;
    this.speed = speed;
    this.fuel = fuel;
}
Car.prototype.rev = function(){
    console.log(this.brand + ' goes brrrrooooommbrroooom')
}
let myCar = new Car('Toyota', 400, 'regular unleaded')

myCar.rev();
console.log(myCar instanceof Car)
console.log(myCar instanceof Array)
myArray = ['h', 'a','p','p','y',' ','b','i','r','t','h','d','a','y']
console.log(myArray.join(''))