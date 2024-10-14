# longest consecutive sequnce
# use a set to keep a track of how everything is sorted

nums = [100, 4, 200, 1, 3, 2, 5]

class Solution:
    def longestConsecutive(self, nums):
      numsSet = set(nums)
      
      seq = []
      longest = 0
      for i in nums:
        if (i-1) not in numsSet:
          length = 0
          while i + length in numsSet:
            length += 1
          longest = max(length, longest)
      print(longest)

      
      
sol = Solution()
sol.longestConsecutive(nums)