# A singly linked list is like
# a -> b -> c
# Creating a linked list in python
# You would have a class Node
# which has 
# Node.value
# Node.next -> referrence to a different object


class SingleNode:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next
    
  def __str__(self):
    return str(self.val)
  

Head = SingleNode(1)
A = SingleNode(3)
B = SingleNode(4)
C = SingleNode(7)

Head.next = A
A.next = B
B.next = C

# Traversing the list
def traverse(head):
  print(head.val)
  if head.next == None:
    return
  traverse(head.next)
  
traverse(Head)


class DoublyLinkedList:
  def __init__(self, val, next, prev):
    self.val = val
    self.prev = prev
    self.next = next
  