class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefix_sum = [0] * n
        arr = list(map(ord,list(s)))

        for shift in shifts:
            prefix_sum[shift[0]] -= 1 if shift[2] == 0 else -1
            if shift[1] + 1 < n:
                prefix_sum[shift[1]+1] += 1 if shift[2] == 0 else -1 

        for i in range(1,n):
            prefix_sum[i] = prefix_sum[i-1] + prefix_sum[i]

        for i in range(n):
            arr[i] = chr((arr[i] + prefix_sum[i] - 97) % 26 + 97)

        return "".join(arr)

