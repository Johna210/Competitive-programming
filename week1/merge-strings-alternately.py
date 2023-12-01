class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        index = 0

        if len(word1) < len(word2):
            min_len = len(word1)

            while index  < len(word1):
                merged += word1[index]
                merged += word2[index]
                index+=1
            
            if len(word2) > min_len:
                merged += word2[index:]
        else:
            min_len = len(word2)

            while index < len(word2):
                merged += word1[index]
                merged += word2[index]
                index+=1
                
            if len(word1) > min_len:
                merged += word1[index:]

        return merged