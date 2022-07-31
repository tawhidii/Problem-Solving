class Solution:
    # def twoSum(self, numbers, target):
    #     left_pointer = 0
    #     right_pointer = len(numbers) - 1
    #     while(left_pointer<right_pointer):
    #         sum_ = numbers[left_pointer] + numbers[right_pointer]
    #         if sum_ == target:
    #             return [left_pointer+1,right_pointer+1]
    #         if sum_ > target:
    #             right_pointer -=1
    #         else:
    #             left_pointer +=1 
        
    #     return []

    # Solution with hashmap 
     def twoSum(self, nums, target):
        seen = {}
        for idx in range(len(nums)):
            remaining = target - nums[idx]
            if remaining in seen:
                return [seen[remaining]+1, idx+1]
            seen[nums[idx]] = idx

        
    

s = Solution()
print(s.twoSum([2,7,11,15],9))





            
