let titles = document.querySelectoAll(".title")

const toggleContent = function(evt){
    evt.target.classList.toggle(".title")
}
let clickFunction = function(evt)
titles.forEach(function(title){
    title.onclick = clickFunction
    title.nextElementSibling.classList.add("hidden")
})
