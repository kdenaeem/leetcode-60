from collections import defaultdict

# given an Array string str, group the anagrams together
# sliding window two for loops and
# 
# all anagrams have the same length
# Use a python dictionary where the keys are sorted strings and the values is the list of all the original strings 
# that when sorted are the key
# this allows you to do in 1 pass
# this solution uses defaultdict because defaultdict allows you to specify the default value
# when a key has no value
#  
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

        