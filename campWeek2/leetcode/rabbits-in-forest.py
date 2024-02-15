class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counts = defaultdict(int)
        for answer in answers:
            counts[answer] += 1

        outputs = 0
        for count in counts:
            outputs += (math.ceil(counts[count] / (count+1)) * (count + 1))

        return outputs