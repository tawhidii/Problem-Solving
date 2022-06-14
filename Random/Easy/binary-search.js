var search = function(nums, target) {
    var start = 0;
    var end = nums.length - 1
    var middle = Math.floor((start+end)/2)
    while(nums[middle] !== target && start<=end){
        if(target>nums[middle]){
            start = middle + 1
        }else{
            end = middle - 1
        }
        middle = Math.floor((start+end)/2)
    }
    if(nums[middle]==target){
        return middle
    }else{
        return -1
    }


};

search([-1,0,3,5,9,12],9)



