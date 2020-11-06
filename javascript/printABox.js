const printSquare = function(side1,side2){
    var s = ""
    var p = ""
    for(let i = 0; i < side1; i++){
        myVar = []
        s += "-"
    }console.log(s)
    for(let j = 0; j < side2; j++){
        if (j == 0 || j == side2.lenth - 1) {
            console.log('|' +  "   " + '|')
        }else{
            myVar.push('')
            console.log(myVar.join('')) 
    }
}
    for (let k = 0; k < side1; k++){
        p += "-"
    }console.log(p)
}


printSquare(4,5)