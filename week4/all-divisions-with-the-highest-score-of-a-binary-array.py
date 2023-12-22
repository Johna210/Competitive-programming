class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        
        score = max_score = sum(nums)
        highest_scores = [0]
        
        for i, j in enumerate(nums, 1):
            score += 1 if j == 0 else -1
            if score > max_score:
                highest_scores = [i]
                max_score = score
            elif score == max_score:
                highest_scores.append(i)
        
        return highest_scores