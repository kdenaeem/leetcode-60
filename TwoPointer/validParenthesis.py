# using a hashmap and a stack
# we check each bracket and the closing brackets behind it
# iterate through the array and when theres a closing back 
# check if theres a corresponding opening bracket right before 
# it

class Solution(object):
    def isValid(self, s):
        bracketHashmap = {')' : '(', ']' : '[', '}': '{'}
        bracketStack = []
        
        for bracket in s:
            if bracket in bracketHashmap:
                if bracketStack and bracketStack[-1] == bracketHashmap[bracket]:
                    bracketStack.pop()
                else:
                    print("here")
                    return False
            else:
                bracketStack.append(bracket)
        if not bracketStack:
            return True
        else:
            return False        
            
            