function countPositivesSumNegatives(input) {
    if(input == null) return [0,0];
    if(input.length === 0) return [0,0];
    let countPositiveNum = 0;
    let negativeSum = 0;
    for(let value of input){
        if(value>0) countPositiveNum += 1;
        if(value<0) negativeSum += value;
    }
    return [countPositiveNum,negativeSum];
}

let a = countPositivesSumNegatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15])
console.log(a);