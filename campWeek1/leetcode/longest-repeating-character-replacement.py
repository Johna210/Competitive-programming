class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        max_len = 0
        max_count = 0

        for right in range(len(s)):
            counts[s[right]] += 1
            max_count = max(max_count,counts[s[right]])
            
            if max_len - max_count >= k:
                counts[s[right - max_len]] -= 1
            else:
                max_len += 1            
        return max_len

