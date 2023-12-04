class Solution:
    def largestGoodInteger(self, num: str) -> str:
        largest = ""
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                if not largest:
                    largest = num[i:i+3]
                elif int(num[i:i+3]) > int(largest):
                    largest = num[i:i+3]

        return largest
