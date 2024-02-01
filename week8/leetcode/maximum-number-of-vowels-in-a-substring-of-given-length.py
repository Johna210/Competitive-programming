class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        max_value = 0
        count = 0
        vowels = {'a','e','i','o','u'}

        for right in range(len(s)):
            if (right - left +1) > k:
                if s[left] in vowels:
                    count-=1
                left+=1
            if s[right] in vowels:
                count+=1
                max_value = max(max_value,count)
        return max_value