
# the next next greatest element
# is the first greater element in the other array that is 
# to the right of x in the first array

# we just have to find the next variable from the first array in the second one

# create a hashmap for arr1 with the elements and their indexes



class nextGreatest:
  def solution(self, array1, array2):
    res = [[] for i in range(0, len(array1))]
    checkDict = {}
    for i in range(0, len(array1)):
      checkDict[array1[i]] =  i
    print(checkDict)
    
    for j in range(0, len(array2)-1):
      if array2[j] in checkDict:
        for j in range(i + 1, len(array2)):
          if array2[j] > array2[i]:
            res[checkDict.get(array2[i], 0)] = array2[j]
            
            
        
      

sol = nextGreatest()
sol.solution([4,1,2], [1,3,4,2])