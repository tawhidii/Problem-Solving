const persistence = (num) => {
    let count = 0;
    let numToStr = num.toString()
    let multiply = 1;
    while(numToStr.length>1){
        numToStr.split('').map(item=>{
            multiply = multiply * item
            numToStr = multiply.toString()
        })
        multiply = 1;
        count++
    }
    return count
}
   


persistence(39)