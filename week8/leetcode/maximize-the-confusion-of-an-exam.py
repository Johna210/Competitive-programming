class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = right = 0
        values = {'T':0,'F':0}
        result = 0

        for right in range(len(answerKey)):
            values[answerKey[right]] += 1
            if (right-left+1) - max(values['T'],values['F']) <= k:
                result = max(result,right-left+1)

            else:
                values[answerKey[left]] -= 1
                left += 1

        return result
