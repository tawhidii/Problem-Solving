var buildArray = function (nums) {
    let ans = []
    nums.forEach((num, index) => {
        ans.push(nums[nums[index]])
    })
    return ans
};

