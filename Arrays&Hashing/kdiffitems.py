class Solution:
  def findPairs(nums, k):
    nums1 = Counter(nums)
    count = 0
    if k == 0:
      for keys, v in nums1.items():
        if v > 1:
          count += 1
    else:
      for keys, v in nums1.items():
        if keys+k in nums1:
          count += 1
    return nums
      