class Solution:
    def sortSentence(self, s: str) -> str:
        d ={}
        ans = []
        s = s.split(" ")
        s.sort(key=lambda x: x[-1])

        for i in range(len(s)):
            s[i] = s[i][:-1]
        # for i in s:
        #     d[int(i[-1])] = i[:-1]

        # l = len(d)
        
        # for j in range(1,l+1):
        #     ans.append(d[j])

        return " ".join(s)