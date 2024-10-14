class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for n in tokens:
          if n == "+":
            firstNum = int(stack.pop())
            secondNum = int(stack.pop())
            n = firstNum + secondNum
          if n == "/":
            firstNum = stack.pop()
            secondNum = stack.pop()
            n = int(float(secondNum) / firstNum)
          if n == "*":
            firstNum = int(stack.pop())
            secondNum= int(stack.pop())
            n = secondNum * firstNum

          stack.append(n)
        return stack[0]

sol = Solution()
print(sol.evalRPN(["18"]))