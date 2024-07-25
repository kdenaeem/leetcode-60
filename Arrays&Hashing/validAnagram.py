# Given two string s and t return true, if t is an anagram of s then return true

class Solution(object):
    def isAnagram(self, s, t):
        if (len(s) != len(t)):
            return False
        print(s[::-1])
        set1 = set()
        for char in s:
            set1.add(char)
        beforeLength = len(set1)
        for char in t:
            set1.add(char)
        if len(set1) == beforeLength:
            return True
        return False
sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))        