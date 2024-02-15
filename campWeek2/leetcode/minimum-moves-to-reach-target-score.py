class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if maxDoubles == 0:
            return target - 1
        count = 0
        while maxDoubles > 0 and target > 1:
            if target % 2 != 0:
                count+=1
                target-=1
            else:
                maxDoubles -= 1
                target -= (target // 2)
                count+=1
        
        return count + (target-1)
