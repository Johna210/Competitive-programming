class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # left = 0
        # right = len(s) - 1

        # while left < right:
        #     s[left] , s[right] = s[right],s[left]
        #     left+=1
        #     right-=1

        for i in range(len(s) // 2):
            s[i] , s[len(s)-i-1] = s[len(s)-i-1] , s[i]