# we will be using the bucket sort for this problem
# 
# list 
# this list index will store the number of occurences 
# and the list values will store the actual value
# first we will create the dictionary using the key as the 
# value as the occurence

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(0, len(nums)+1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # now we have 
        # {1: 2, 2: 3, 3: 3, 4: 3}
        # we need to add this to freq where the key is the value
        # and the value is used as the index

        for n, c in count.items():
            freq[c].append(n)

        # now we have 
        # [[], [[1]], [[2]]]
        # just to reverse the array in reverse order
        res = []
        for i in range(len(freq)- 1, 0, -1):
            print(freq[i])
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res   