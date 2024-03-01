class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def div_conq(i,j):
            if j - i + 1 < 2:
                return (0,-1)
            hashMap = set()
            for k in range(i,j+1):
                hashMap.add(s[k])

            for k in range(i,j+1):
                if s[k].upper() in hashMap and s[k].lower() in hashMap:
                    continue
                left = div_conq(i,k-1)
                right = div_conq(k+1,j)
                return left if (left[1] - left[0] + 1) >= (right[1] - right[0] + 1) else right

            return (i,j)

        N = len(s)
        left, right =  div_conq(0,N-1)  

        return s[left:right+1]            
        