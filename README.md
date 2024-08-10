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

