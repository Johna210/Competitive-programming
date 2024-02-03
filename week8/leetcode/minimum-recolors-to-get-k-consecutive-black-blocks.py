class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        counts = []
        left = 0
        right = k

        while right <= len(blocks):
            counts.append(blocks[left:right].count("W"))
            left += 1
            right += 1

        return min(counts)