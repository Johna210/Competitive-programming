class Solution:
    def largestOddNumber(self, num: str) -> str:
        index = len(num) - 1
        while index > -1 and int(num[index]) % 2 == 0:
            index -= 1
        return num[:index + 1] 