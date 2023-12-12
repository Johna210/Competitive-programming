class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        val = s.split()

        left = 0
        right = len(val) - 1

        while left < right:
            val[left], val[right] = val[right], val[left]
            left+=1
            right-=1

        return " ".join(val)