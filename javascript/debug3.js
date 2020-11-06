let ships = [    
    {
        name:"x-wing",
        topSpeed:98,
        acceleration:3,
        cargoCapacity:0
    },
    {
        name:"carillion",
        topSpeed:100,
        acceleration:4,
        cargoCapacity:2
    },
    {
        name:"tie-figher",
        topSpeed:89,
        acceleration:2,
        cargoCapacity:1
    }
]

ships.forEach(function(ship){
    console.log("**********")
    for(key in ship){
        console.log(` ${key} : ${ship[key]} `)
    }
    console.log("**********")
})