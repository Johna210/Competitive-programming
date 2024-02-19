class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        counts = defaultdict(lambda : -1)
        new_arr = [0] * (2*len(nums))
        stack = []
        n = len(nums)
        for i in range(2*n):
            new_arr[i] = nums[i%n] 

        for i in range(2*n):
            while stack and new_arr[stack[-1]] < new_arr[i]:
                counts[stack.pop()] = i%n
            
            stack.append(i%n)

        output = [0] * n
        for i in range(n):
            if i in counts:
                output[i] = nums[counts[i]]
            else:
                output[i] = -1

        return output