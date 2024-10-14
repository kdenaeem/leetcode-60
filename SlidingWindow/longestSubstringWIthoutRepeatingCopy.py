# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

# Input: s = "abcabcbb"
# Output: 3

# This is a sliding window problem

# we have a string and we need to find the longest subset
# using sliding window, we can create a set which keeps track of which characters
# have already been added. If we reach a character where we witness it again
# we can reset the count.

class Solution:
    def lengthOfLongestSubstring(self, s: str):
      longest = 0
      charSet = set()
      l = 0
      for r in range(0, len(s)):
        if s[r] in charSet:
          charSet.remove(s[l])
          l += 1
          
        charSet.add(s[r])
        longest = max(longest, len(charSet))
      print(longest)
sol = Solution()
sol.lengthOfLongestSubstring("11111")
