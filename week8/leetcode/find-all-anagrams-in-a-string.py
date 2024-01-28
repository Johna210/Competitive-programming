class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        target = Counter(p)
        cur = Counter()

        output = []
        for idx, c in enumerate(s):
            cur.update(c)
            if idx >= len(p):
                cur.subtract(s[idx - len(p)])
            if cur == target:
                output.append(idx - len(p) + 1)
        return output
