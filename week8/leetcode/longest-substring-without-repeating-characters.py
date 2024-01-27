class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        substring = set()
        max_length = 0
        left = 0

        for i in range(len(s)):
            while s[i] in substring:
                substring.remove(s[left])
                left+=1

            substring.add(s[i])
            max_length = max(max_length,len(substring))
        
        return max_length