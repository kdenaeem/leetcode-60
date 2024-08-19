# here we are using the two pointer technique and a while loop
# one algorithm starts at the top and the other starts at the end of the list 


class Solution:
    def twoSum(self, numbers, target):
      l, r = 0, len(numbers)-1
      while l < r:
        print(l, r)
        curSum = numbers[l] + numbers[r]
        if curSum > target:
            r = r -1 
        elif curSum < target:
            l = l + 1
        else: 
          return [l + 1, r + 1]

numbers = [2,7,11,15]
sol = Solution()
sol.twoSum(numbers, 9)