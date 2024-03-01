class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def pow(n):
            if n == 1:
                return True
            elif n < 4:
                return False

            return pow(n/4)
        
        return pow(n)