function sumOfDifferences(arr) {
    let sortedArr = arr.sort((a,b)=>b-a);
    let sum_ = 0;
    for(let i=0;i<sortedArr.length-1;i++){
        let minus = sortedArr[i] - sortedArr[i+1];
        sum_ += minus;
    }
    return sum_;
}

console.log(sumOfDifferences([1, 2, 10]))