class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * n
        prefix = [0] * n
        postfix = [0] * n

        prefix[0] = nums[0]
        for i in range(1,n):
            prefix[i] = prefix[i-1] + nums[i]
        
        postfix[-1] = nums[-1]
        for i in range(n-2,-1,-1):
            postfix[i] = postfix[i+1] + nums[i]

        output[0] = abs(nums[0] * n - postfix[0])
        output[-1] = abs(nums[-1] * n - prefix[-1])

        for i in range(1,len(output)-1):
            value1 = abs((nums[i] * (n-i)) - postfix[i])
            value2 = abs((nums[i]*i) - prefix[i-1])
            output[i] = value1 + value2

        return output