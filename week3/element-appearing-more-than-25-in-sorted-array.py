class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counts = {}

        for i in range(len(arr)):
            if arr[i] in counts:
                counts[arr[i]]+=1
                
            else:
                counts[arr[i]] = 1
               
            if counts[arr[i]] / len(arr) > 0.25:
                    return arr[i]