class Solution:
    def balancedString(self, s: str) -> int:
        N = len(s)
        count = Counter(s)
        left = 0
        req = N // 4
        res = inf
        for right in range(N):
            count[s[right]] -= 1
            while left < N and count['W'] <= req and count['Q'] <= req and count['E'] <= req and count['R'] <= req:
                res = min(res, right - left + 1)
                count[s[left]] += 1
                left += 1
        return res
        