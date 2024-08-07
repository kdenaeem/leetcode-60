# The way to think about this is
# you have two arrays
# where one is 1 | 1 * a | 1 * a * b | 1 * a * b * c
# and another is d*b*c | d*b | d | 1
# when you multiply these together you get exclusion from one
# the trick here is 

class Solution(object):
    def productExceptSelf(self, nums):
        res = [1] * len(nums)
        prefix = 1
        for i in range(0, len(nums)):
            res[i] = res[i] * prefix
            prefix = prefix * nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * postfix
            postfix = postfix * nums[i]
        return res
        