class Solution:
    def reverse(self, x: int) -> int:
        length = (len(str(x))-1)
        digits = []
        value = 0

        if x > 0:
            while x > 0:
                digits.append(x%(10))
                x = x // 10

            for i in digits:
                
                value += i *(10**length)
                length-= 1
        
        else:
            length -= 1
            x *= -1
            while x > 0:
                digits.append(x%(10))
                x = x // 10

            for i in digits:
                
                value += i *(10**length)
                length-= 1
            value *= -1
        if abs(value) >= 2147483647:
            return 0
        return value
