let value = 5;

if(value === 3){
    console.log("this equal 3")
}
else if(value === 4){
    console.log('this equals 4')
}
else{
    console.log('this always equalled 5')
}

let num1 = 2, num2 = 4;
result = num1>num2 ? 'higher': 'lower'

let temp = 78;
let color;
switch(true){
    case (temp < 0):
    color = "#39316e"
    break;
    case (temp > 0 && temp < 30):
    color = "#5870a8"
    break;
    case (temp > 29 && temp < 50):
    color = "#589ea8"
    break;
    case (temp > 49 && temp < 75):
    color = "#58a885"
    break;
    case (temp > 74 && temp < 80):
    color = "#58a85d"
    break;
    case (temp > 74 && temp < 80):
    color = "#d6d25a"
    break;
    case (temp > 79 && temp < 90):
    color = "#e08460"
    break;
    default:
        color = "#eb6060"
}
console.log(color)

let i = 0;
let j;
while(i < 10){
    j += i
    i++
}
console.log(j)

for(var i = 5; i = 10; i++ ){
    console.log(i)
}


j = 20
for(let i = 6; i > 1; i--){
    j = j/i;
    console.log(j);
}

let j;
for (let i = 30; i > 0; i--){
    if (!((i%2) && (i%3))) continue;
    else{
        j += i
    }
}
console.log(j)