from collections import defaultdict

# given an Array string str, group the anagrams together
# sliding window two for loops and
# 
# using a default dict
# join the characters in alphabetical order
# use this as a key
# then append the words to the key that match it
class Solution(object):
        
        def groupAnagram(self, strs):
              anagram = defaultdict(list)
              for ele in strs:
                    ch = ''.join(sorted(ele))
                    if (anagram.get(ch)) == None:
                        anagram[ch] = [ele]
                    else:
                          val = anagram.get(ch)
                          val.append(ele)
              final_list = []
              for k in anagram.values():
                  final_list.append(k)
              return final_list             



sol1 = Solution()             
strs = ["eat","tea","tan","ate","nat","bat"]
dict1 = (sol1.groupAnagram(strs))

        