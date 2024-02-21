class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = (10**9) + 7
        num = n // 2
        pow_5 = pow_4 = num

        if n % 2:
            pow_5+=1
        return pow(5,pow_5,MOD) * pow(4,pow_4,MOD) %MOD
        