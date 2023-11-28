class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_to_t = {}

        for index in range(len(s)):
            if s[index] in s_to_t and s_to_t[s[index]] != t[index]:
                return False
            else:
                s_to_t[s[index]] = t[index]

        t_to_s = {}

        for index in range(len(t)):
            if t[index] in t_to_s and t_to_s[t[index]] != s[index]:
                return False
            else:
                t_to_s[t[index]] = s[index]

        return True

