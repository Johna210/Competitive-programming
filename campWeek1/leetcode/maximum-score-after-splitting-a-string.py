class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        postfix = [0] * (n)
        postfix[-1] = int(s[-1])

        for i in range(n-2,0,-1):
            postfix[i] = postfix[i+1] + int(s[i])

        prefix = [0] * (n)
        prefix[0] = 1 if s[0] == '0' else 0
        for i in range(1,n-1):
            prefix[i] = prefix[i-1] + 1 if s[i] == '0'else  prefix[i-1]

        prefix.pop()
        postfix.pop(0)

        value = 0
        for i in range(len(prefix)):
            value = max(value,prefix[i] + postfix[i])
        
        return value
