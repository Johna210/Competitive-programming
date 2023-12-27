class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counts = {}
        for i in range(len(arr2)):
            counts[arr2[i]] = i
        def customComparator(item):
            if item not in counts:
                return len(arr2) + item
            return counts[item]
            
        arr1.sort(key = customComparator)
        return arr1