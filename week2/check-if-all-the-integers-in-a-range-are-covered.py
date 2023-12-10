class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        sets = set()

        for i in range(len(ranges)):
            for j in range(ranges[i][0],ranges[i][1]+1):
                sets.add(j)

        for k in range(left,right+1):
            if k not in sets:
                return False

        return True

        
                
