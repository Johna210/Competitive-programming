class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        first = 0
        second = 0

        min_len = min(len(nums1),len(nums2))
        output = -1
        while first < len(nums1) and second < len(nums2):
            if nums1[first] == nums2[second]:
                output = nums1[first]
                break
            elif nums1[first] > nums2[second]:
                second+=1

            else:
                first+=1

        return output