# leetcode-60

Tricks

Traversing through an array left to right
And then Right to Left

```python
        for i in range(0, len(nums)):
            res[i] = res[i] * prefix
            prefix = prefix * nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i] * postfix
            postfix = postfix * nums[i]
```

using 
```python
while (n + counter) ..:
  country += 1
  ```
  is a way to lock into a sequnce in a list
  you can do a for loop and then lock in

Stacks
You can implement a stack using a linked list or an array. 
In python, we will use an array which is built like a stack already


# Recursion
All recursive functions need a base case and it needs to be the first 
condition thats evaluated. 
And each partially completed funciton is stored in memory until the base 
function is returned. 

# Different types of techniques to solve problems
Recursion, Divide-Conquer, Dynamic programming, greedy algorithm

Merge sort is a type of Divide-Conquer algorithm that can be used to 
continuously divide an unsorted array into smaller sub problems

The sub problems divided by the ranking algorithm are supposed to be non
repeating. But if there are duplicates then dynamic programming is used 

In order to really understand recursion, split a big problem into its most basic sub problem. What needs to be added, what needs to changed. 
Recursion solves the problem vertically and solves the sub programs heirachaly
whereas enumerations divides the problem horizontlly and solves the sub problems one by one

The two things to focus on for recursion is an end condition and self invocation

the end condition gives the answer to the most basic sub problem
and the self invocation is for solving sub problems

# Traversing a binary tree
void traverse(TreeRoot node) {
  if root == null
  return;
  traverse(node.left)
  traverse(node.right)
}

# traversing an n fork tree
void traverse(TreeRoot node) {
  if root == nullptr 
  return;
  for child in root:
  traverse(node.child)
}

