
console.log('hello')
let body = document.querySelector('#main')
console.log(body)
let header = document.createElement('h1')
let section = document.createElement('section')
let headerTwo = document.createElement('h2')
let paragraph = document.createElement('p')
let myList = document.createElement('ul')
body.append(header)
header.innerHTML = "this is a string"
body.append(myList)
for(i = 0; i < 5; i++){
    let l = document.createElement('li')
    l.append(`This is item #${i}`)
    myList.append(l)
}
myList.style.color = 'red'
myList.style.fontFamily = 'sans serif';


