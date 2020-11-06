counter = 1
let button = document.querySelector('.btn')
button.innerHTML = counter
button.classList.add('button')

const func1 = function(){
    counter++
    
    button.innerHTML = counter
    if(counter > 9){
        button.removeEventListener('click', func1)
        button.classList.replace('button','secondary')
        
    }else{
        button.innerHTML = counter
        button.style.fontSize = ((counter*25)+"px")
    }
};


button.addEventListener('click',func1);
