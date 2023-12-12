class Solution:
    def isHappy(self, n: int) -> bool:
        checked = set()
        num = n
        while True:
            val = 0
            while num > 0:
                val += (num % 10)**2
                num = num // 10 

            num = val

            if num == 1:
                return True
            elif num  in checked:
                return False
            else:
                checked.add(num)
