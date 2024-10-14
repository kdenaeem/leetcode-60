# we want to find the frequency of items 
# and then find the top number of those
# this will be done using a bucket sort using a dictory
# so have a dictionary where the key is number of occurences
[
  [2, 3],
  [1, 3],
  [5],
]

# where the frequency is the index of the array
# in order to create this list
# we can create an array 
# 
{
  1: 2,
  2: 1,
  3: 7,
  4: 9
}

# this can be easily created just doing count[n] = count.get(n, 0) + 1

class Solution:
    def topKFrequent(self, nums, k):
      freq = [[] for i in range(0, len(nums))]
      
      count = {}
      
      for i in range(0, len(nums)-1):
        count[nums[i]] = 1 + count.get(nums[i], 0)
      
      
      for items,key in count.items():
        freq[key].append(items)
        
      res = []
      for i in range(len(freq)-1, 0, -1):
        for j in freq[i]:
          res.append(j)
          if len(res) == k:
            print(res)
            return res
      
sol = Solution()
sol.topKFrequent([1,1,3,5,6,1,6], 2)
      

