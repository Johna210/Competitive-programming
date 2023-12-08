class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        values = {}
        output = []
        for i in range(len(list1)):
            if list1[i] in list2:
                val = i + list2.index(list1[i])
                values[list1[i]] = val 
        minimum = min(values.values())
        for value in values:
            if values[value] == minimum:
                output.append(value)
        return output