var arrSum = function(numsArr){
    var totalSum = 0;
    for(var value of numsArr){
        totalSum += value;
    }
    return totalSum;
}


var pivotIndex = function(nums) {
    let total = arrSum(nums);
    let leftSum = 0;
    for(let index in nums){
        total -= nums[index]
        if(total == leftSum){
            return index
        }else{
            leftSum += nums[index]
        }
    }
    return -1

};

console.log(pivotIndex([1,7,3,6,5,6]))