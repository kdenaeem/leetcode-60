# Given an integer of nums and an integer target nums
# return indices of two numbers such that they add up to the target

# For this loop through the nums and using sliding window
# i and j
# if i + j = target then return indices i and j
# conditions . !(i=j) 

class Solution(object):
    def twoSum(self, nums, target):
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                print(nums[i] + nums[j], i, i)
                if (nums[i]!=nums[j]) and (nums[i]+nums[j]==target):
                    return [i,j]
        
                

sol = Solution()
print(sol.twoSum([3,2,4], 6))
                    
                
        
        