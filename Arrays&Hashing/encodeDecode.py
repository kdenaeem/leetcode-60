class Solution:

    def encode(self, strs):
        res = ""
        for s in strs:
          res += str(len(s)) + '£' + s
        print(res)        
        return res
    def decode(self, s):
      res = []
      i = 0
      while i < len(s):
        j = i 
        while (s[j] != "£"):
          j += 1
        length = int(s[i:j])
        res.append(s[j+1:j+length+1])
        i = j + 1 + length
      
      return res


sol = Solution()
res = sol.encode(["neet","code","love","you"])
print(sol.decode(res))