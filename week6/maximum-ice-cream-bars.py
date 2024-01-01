class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()

        output = 0
       
        i  = 0
        while i < len(costs):
            if coins < costs[i]:
                break
            output+=1
            coins = coins - costs[i]
            i+=1

        return output
