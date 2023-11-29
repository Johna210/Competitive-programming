class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        number = n
        while True:
            if n % 2 == 0 and n % number == 0:
                return n
            n+=1
        # return (2 * n) // gcd(2, n)
        