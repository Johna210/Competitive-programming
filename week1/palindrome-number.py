class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x
        reverse = 0

        while x >= 1:
            reverse *= 10
            reverse += (x % 10)
            x = x // 10

        return num == reverse