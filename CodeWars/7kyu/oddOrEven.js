function oddOrEven(array) {
    //enter code here
    const sum = array.reduce(doSum,0);
    function doSum(accumulator,a){
        return Math.abs(accumulator+a)
    }
    if(sum%2==0){
        return "even"
    }else{
        return "odd"
    }
    
}


console.log(oddOrEven([0, 1, 4]))