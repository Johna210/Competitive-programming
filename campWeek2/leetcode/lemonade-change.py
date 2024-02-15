class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        values = {5:0,10:0}
        for bill in bills:
            if bill == 5:
                values[5] += 1
            elif bill == 10:
                if values[5] >= 1:
                    values[5] -= 1
                else:
                    return False
                values[10] += 1
            elif bill == 20:
                if values[10] >= 1 and values[5] >= 1:
                    values[5] -= 1
                    values[10] -= 1
                elif values[10] < 1 and values[5] >= 3:
                    values[5] -= 3
                else:
                    return False

        return True