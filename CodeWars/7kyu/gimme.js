function gimme (triplet) {
    let myArr = [...triplet]
    let sorted = triplet.sort((a,b)=>a-b)
    return myArr.indexOf(sorted[1])
}

console.log(gimme([2, 3, 1]))