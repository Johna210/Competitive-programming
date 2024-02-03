class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for right in range(len(haystack)):
            if haystack[right:right+len(needle)] == needle:
                return right

        return -1
                    


