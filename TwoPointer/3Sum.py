class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [] 
        nums.sort()
        
        for i, a in enumerate(nums):
          # skip duplicates
          if i > 0 and a == nums[i-1]:
            continue
          l, r = i + 1, len(nums) -1
          while l < r:
            sumthree = a + nums[l] + nums[r]
            print([a, nums[l], nums[r]])
            if sumthree > 0:
              r -= 1
            elif sumthree < 0:
              l += 1
            else:
              res.append([a, nums[l], nums[r]])
              l += 1
              r -= 1
                
        return res

          
            
            

nums = [-1,0,1,2,-1,-4]
print(nums.sort())
print(nums)
# print(nums[0])
sol = Solution()
sol.threeSum(nums)