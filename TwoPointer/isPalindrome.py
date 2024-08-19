import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub('[^a-zA-Z0-9]+', '', s)
        s_reverse = s[::-1]
        print(s_reverse)
        print(s)
        if s_reverse.lower() == s.lower():
            return True
        return False
        
