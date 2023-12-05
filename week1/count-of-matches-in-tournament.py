class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0

        while n > 1:
            left = n % 2
            n = (n // 2) + left
            matches += (n-left) 

        return matches