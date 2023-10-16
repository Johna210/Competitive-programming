class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        values = {}
        for i in s:
            if i in values:
                values[i] += 1
            else:
                values[i] = 1

        for i in t:
            if i not in values or values[i] <= 0:
                return False
            values[i] -= 1
        

        return len(s) == len(t)
         
        
