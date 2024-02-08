class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefix = [0] * n
        for booking in bookings:
            prefix[booking[0]-1] += booking[2]
            if booking[1] < n:
                prefix[booking[1]] -= booking[2]

        for i in range(1,n):
            prefix[i] += prefix[i-1] 

        return prefix
