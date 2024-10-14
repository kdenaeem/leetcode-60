# binary search with sliding window
# create a window using l and r, check if value m + k is better than current


class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k
        m = 0

        while l < r:
            m = l + (r - l) // 2
            if x - arr[m] > arr[m+k] - x:
                l = m + 1
            else:
                r = m
        return arr[l:l+k]
