class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        output = []
        for i in range(0,len(nums)-1,2):
            output+=([nums[i+1]]*nums[i])
        return output