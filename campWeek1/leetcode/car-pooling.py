class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = max(trips, key = lambda a: a[2])[2]
        prefix = [0] * n
        for trip in trips:
            prefix[trip[1]] += trip[0]
            if trip[2] < n:
                prefix[trip[2]] -= trip[0]

        if prefix[0] > capacity:
            return False

        for i in range(1,n):
            prefix[i] += prefix[i-1]
            if prefix[i] > capacity:
                return False
        return True


        