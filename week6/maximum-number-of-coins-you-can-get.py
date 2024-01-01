class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        value = 0
        piles.sort()

        while len(piles) >= 3:
            
            value += piles[len(piles) - 2]
            piles.pop(len(piles) - 2)
            piles.pop(0)
            piles.pop(len(piles)-1)
        return value


        # return sum(sorted(piles, reverse=True)[1:len(piles)*2//3:2])