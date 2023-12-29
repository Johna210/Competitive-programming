class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # def comparator(item):
        #     x = item // (10**(len(str(item))-1))
        #     return x
        # nums.sort(key=comparator,reverse=True)

        # d = defaultdict(list)
        # for num in nums:
        #     i = str(num)[0]
        #     d[i].append(str(num) )
        # print(d)
        # lst = []

        # print(nums)

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if str(nums[i]) + str(nums[j]) > str(nums[j]) + str(nums[i]):
                    continue
                else:
                    nums[i] , nums[j] = nums[j] , nums[i]
        if sum(nums) == 0:
            return "0"
        return "".join(str(num) for num in nums)