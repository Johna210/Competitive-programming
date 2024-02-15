class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = defaultdict(int)
        for letter in s:
            counts[letter] += 1

        length = 0
        ones = 0

        for count in counts:
            if counts[count] % 2 == 0:
                length += counts[count]
            elif counts[count] > 1:
                length += (counts[count] - 1)
                ones+=1
            else:
                ones+=1

        return length + 1 if ones else length
