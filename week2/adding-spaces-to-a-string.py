class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        edited = ""
        start = 0

        for i in spaces:
            edited += s[start:i] + " "
            start = i
        edited += s[start:]
        
        return edited