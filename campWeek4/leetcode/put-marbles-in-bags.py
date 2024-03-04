class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if len(weights) == 1:
            return 0
        
        pair_sum = []
        for i in range(len(weights)-1):
            pair_sum.append(weights[i]+weights[i+1])
        pair_sum.sort()

        mini_sum = sum(pair_sum[:k-1])
        maxi_sum = sum(pair_sum[len(pair_sum)-k+1:])

        return maxi_sum - mini_sum