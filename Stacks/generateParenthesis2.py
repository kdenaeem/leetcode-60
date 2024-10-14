# generate an array of all possible numbers of bracket combinations given
# an integer n. 
# this is a recursion problem
# and your supposed to create all the different permutation


class Solution:
    def generateParenthesis(self, n):
      # this stack will store each permutation
      stack = []
      res = []
      
      # using openN and closeN call backtrack by keeping track
      # of how many open and how many closed we have already done
      # we do it until the open reaches a certain amount
      # closed is only called when closedN is less than openN
      # each time the recursion comes back, we pop a bracket
      def backtrack(openN, closeN):
        if openN == closeN == n:
          res.append("".join(stack))
          return 
        
        if openN < n:
          stack.append("(")
          backtrack(openN+1, closeN)
          # pop the last item in the stacks once a combination is found
          stack.pop()
          
        if closeN < openN:
          stack.append(")")
          backtrack(openN, closeN+1)
          stack.pop()
      
      backtrack(0, 0)
      print(res)
        
          
sol = Solution()
sol.generateParenthesis(3)