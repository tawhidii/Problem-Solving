const findOutlier = (integers) => {
    let OddArr = [];
    let evenArr = [];
    integers.forEach(num=>{
        num % 2 === 0 ? evenArr.push(num) : OddArr.push(num)
    })
    const result = evenArr.length === 1 ? evenArr[0] : OddArr[0]
    return result;
}

let ans = findOutlier([160, 3, 1719, 19, 11, 13, -21]);
console.log(ans)