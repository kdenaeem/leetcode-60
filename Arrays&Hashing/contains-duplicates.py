# Given an array, return true if a value appears more than once in the array
# use a set and if the set has duplicates then the length wont be the same

import typing

class Solution:
  def hasDuplicates(self, nums: typing.List[int]) -> bool:
    checkSet = set()
    for i in nums:
      checkSet.add(i)
    
    if (len(checkSet)) != len(nums):
      return True
    return False

