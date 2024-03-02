class Solution:
    def minWindow(self, s: str, t: str) -> str:
        N = len(s)
        if t == "":
            return ""
        required = Counter(t)
        window = {}
        min_len = inf
        substring = (0,0)
        have = 0
        need = len(required)
        # Set our window with the letter of the required chars
        for char in required:
            window[char] = 0

        left = 0
        for right in range(N):
            # if the char is in required add it in our window
            # And if it satisfy our need increment the have variable 
            # That holds how many letters we have from our neeeded
            if s[right] in required:
                window[s[right]] += 1
                if window[s[right]] == required[s[right]]:
                    have+=1
            # If we have all the needed letters
            # Shring our window till we dont have all letters
            while have == need:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    substring = (left,right)
                if s[left] in window:
                    window[s[left]] -= 1
                    if window[s[left]] < required[s[left]]:
                        have-=1
                left+=1

        return s[substring[0]:substring[1]+1] if min_len != inf else ""




        