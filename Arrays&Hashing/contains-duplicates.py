# Given an array, return true if a value appears more than once in the array

import typing

class Solution:
  def hasDuplicates(self, nums: typing.List[int]) -> bool:
    checkSet = set()
    for i in nums:
      checkSet.add(i)
    
    if (len(checkSet)) != len(nums):
      return True
    return False

