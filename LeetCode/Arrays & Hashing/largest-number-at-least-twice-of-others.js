

var maximumValue = function(nums){
    let maxValue = 0;
    for(let index in nums){
        if(nums[index]>maxValue){
            maxValue = nums[index]
        }
    }
    return maxValue
}

var dominantIndex = function(nums) {
    let maxItem = maximumValue(nums);
    let idx = nums.indexOf(maxItem);
    let count = 0;
    nums.splice(idx,1)
    for(let val of nums){
        if(maxItem>= val*2){
            count +=1
        }
    }
    if(count==nums.length){
        return idx
    }else{
        return -1
    }
    
    
};
dominantIndex([3,6,1,0])