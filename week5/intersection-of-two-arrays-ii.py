class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        nums1.sort()
        nums2.sort()

        first = second = 0
        while first < len(nums1) and second < len(nums2):
            if nums1[first] < nums2[second]:
                first+=1
            elif nums2[second] < nums1[first]:
                second+=1
            else:
                output.append(nums1[first])
                first+=1
                second+=1
            
        return output