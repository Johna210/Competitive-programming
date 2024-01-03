class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        counts = 0
        first = 0
        second = 0

        while first < len(g) and second < len(s):
            if g[first] <= s[second]:
                counts+=1
                first+=1
            second+=1

        return counts