def rotate_left3(nums):
    middle = nums[1]
    first = nums[0]
    last = nums[-1]
    return [middle, last, first]
