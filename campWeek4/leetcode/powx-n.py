class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x,n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            result = power(x , n // 2)
            result *= result
            return x * result if n % 2 else result
        if n > 0:
            ans = power(x,n)
        else:
            ans = 1 / power(x,-1*n)
        return ans