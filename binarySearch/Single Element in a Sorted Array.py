# find the size of the left size of the array
# by checking the m - 1 if its th second element of a pair

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if ((m - 1 < 0 or nums[m] != nums[m-1]) and 
            (m == len(nums)-1 or nums[m] != nums[m+1])):
                return nums[m]
            leftSize = m - 1 if nums[m] == nums[m-1] else m
            if leftSize%2==1:
                r = m - 1
            else:
                l = m + 1
        return nums[m]
        
        