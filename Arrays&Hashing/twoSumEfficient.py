# Given an integer of nums and an integer target nums
# return indices of two numbers such that they add up to the target

# For this loop through the nums and using sliding window
# i and j
# if i + j = target then return indices i and j
# conditions . !(i=j) 

# You can create a dict and then do (curr_val - target) since dict look ups are constant time
# In python you can use enumerate to for loop through two different functions

class Solution(object):
    def twoSum(self, nums, target):
        hashSet = {}
        for counter, curr_value in enumerate(nums):
            diff = target - curr_value
            if diff in hashSet:
                return [hashSet[diff], counter]
            
            else:
                hashSet[curr_value] = counter
            
            print(hashSet)
                
sol = Solution()
print(sol.twoSum([3,2,4], 6))

        
                                
                
        
        