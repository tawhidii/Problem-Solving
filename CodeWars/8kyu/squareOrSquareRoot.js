function squareOrSquareRoot(array){
    function print(value,index){
        if(Number.isInteger(Math.sqrt(value))){
            array[index] = Math.sqrt(value)
        }else{
            array[index] = Math.pow(value,2)
        }
    }
    array.forEach(print);
    return array;
}

squareOrSquareRoot([4,3,9,7,2,1])