# find a subset of longest sequence of numbers in an array nums
# We can do this using a set, and by adding each value 
# of the list into the set
# then check if a number one bigger exists
# each time check if 
class Solution:
    def longestConsecutive(self, nums):
        numSet = set(nums)
        
        print(numSet)
        longest = 0
        for n in nums:
          # check if the start of sequence
          if (n-1) not in numSet:
            # then we are at the start of a list
            length = 0
            while (n + length) in numSet:
              length += 1
            longest = max(length, longest)
        print(longest)  
sol = Solution()
nums = [2,20,4,10,3,4,5]
print(sol.longestConsecutive(nums))