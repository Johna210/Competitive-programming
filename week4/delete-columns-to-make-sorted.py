class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        i = len(strs[0])
        output = 0
        index = 0

        while index < i:
            for j in range(len(strs)-1):
                if strs[j][index] > strs[j+1][index]:
                    output += 1
                    break
            index+=1
        
        return output