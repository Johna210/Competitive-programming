class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        val = (num//3) -1
        values = []
        if val + (val+1) + (val+2) == num:
            values = [val,val+1,val+2]
        

        return values