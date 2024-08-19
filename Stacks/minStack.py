# A stack doesnt support min Value function
# we push a -2 and we push
# consider each value having a corresponding minimum value
# we have a pointer at each value which says which the minimum value is 
# we need to support 4 operations
# define our arrays in the constructor
class MinStack(object):

    def __init__(self):
        self.minStack = []
        self.stack = []

    def push(self, val: int) -> None:
        # whilst we append, we need to know if theres already a min    
        self.stack.append(val)
        # if minStack is empty just set val to val
        
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        
    def getMin(self):
        return self.minStack[-1]
        
    def pop(self) -> None:
        self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]        

        
obj = MinStack()

print(obj)
obj.push(5)
obj.push(9)
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.getMin())