class Solution:
    def freqAlphabets(self, s: str) -> str:
        values = ""
        right = len(s) - 1
        left = right - 1

        while right >= 0:
            if s[right] == "#":
                val = chr(int(s[left-1:left+1]) + 96)
                left -= 2
                right = left
                values += val
            else:
                values += chr(int(s[right])+96)
                right-=1
            left = right - 1

        return values[::-1]  