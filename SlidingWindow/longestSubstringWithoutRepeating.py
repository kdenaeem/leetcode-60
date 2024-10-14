# add each character into a set
# and every time it increases check if it already exists

# for this sliding window, we use a set to keep a track of our 
# substring


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        longest = 0
        checkSet = set()
        l = 0
        for r in range(0, len(s)):
          while s[r] in checkSet:
            checkSet.remove(s[l])
            l += 1
          checkSet.add(s[r])
          longest = max(longest, len(checkSet))        
        print(longest)

sol = Solution()
sol.lengthOfLongestSubstring("abcab44")