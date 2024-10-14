# given the head, delete all the duplicates in the list 
# and return the list once its sorted

class SingleNode:
  def __init__(self, val, next):
    self.val = val
    self.next = next


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def traverse(node):
          if node and node.next:
            if node.val == node.next.val:
              node.next = node.next.next
              traverse(node.next)
            else:
              traverse(node.next)
            
            
              