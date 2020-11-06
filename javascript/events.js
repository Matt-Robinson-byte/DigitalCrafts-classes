let button = document.querySelector('span')
button.classList.add('button')

document.querySelector('span').onclick = function(evt){
    evt.target.classList.toggle('secondary')
}