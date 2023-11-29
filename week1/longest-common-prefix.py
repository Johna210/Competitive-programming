class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = len(strs[0])

        for string in strs:
            if len(string) < min_len:
                min_len = len(string)

        index = 0
        substring = ""
        while index < min_len:
            char = strs[0][index]
            count = 0
            for word in strs:
                if char == word[index]:
                    count+=1
            if count == len(strs):
                substring+=char
            else:
                break
            
            index+=1
        
        return substring


        