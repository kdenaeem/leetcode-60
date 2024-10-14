class Solution:
    def generateParenthesis(self, n):
        
        stack = []
        res = []
        
        def backtrack(openN, closedN):
          if openN == closedN == n:
            res.append("".join(stack))
            return
          if openN < n:
            stack.append("(")
            backtrack(openN + 1, closedN)
            stack.pop()
          if closedN < openN:
            stack.append(")")
            backtrack(openN, closedN+1)
            stack.pop()
        backtrack(2, 2)
        print(res)
          
          
          
sol = Solution()
sol.generateParenthesis(5)