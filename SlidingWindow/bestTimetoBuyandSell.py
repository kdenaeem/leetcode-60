# input price = [7,1,5,3,6,4] 

# prices[i] is the price on day i
# we want to maximise the profit by choosing a single day 
# to buy one stock 
# choosing a different day to sell it
# using sliding window


# we have two pointers
# l and r 
# and while loop where l < r
# 
# another way to do it
# the right way
# is using the minimum value and the maximum value and taking them away

class BestTimeToBuy:
  def solution(self, nums):
    l, r = 0, 1
    curr_profit = r - l
    max_profit = 0
    
    while r < len(nums):
      curr_profit = nums[r] - nums[l]
      if curr_profit > 0:
        max_profit = max(max_profit, curr_profit)
      else:
        l = r 
      r = r + 1
    print(max_profit)
sol = BestTimeToBuy()
sol.solution([0,1,5,3,9,4])
