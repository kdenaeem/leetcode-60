# You are given a string s and an integer k 
# For longest subset without repeating
# we used two pointers and a sliding window
# we used a character set 
# where we have a left and right pointer
# the charset would remove characters if they already existed,
# so removing duplicates. and then calculate the length
# in order to do this, we can 
# create a set
# three pointers, one left  §§§§§§§§§§§§§§§and one right. One pointer does the replacing.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        replacer = 0
        
          