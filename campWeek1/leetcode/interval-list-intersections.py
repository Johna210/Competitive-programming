class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        output = []

        first = second = 0

        while first < len(firstList) and second < len(secondList):
            curr = [0,0]
            curr[0] = max(firstList[first][0],secondList[second][0])
            curr[1] = min(firstList[first][1],secondList[second][1])
            
            if firstList[first][1] < secondList[second][1]:
                first+=1
            elif firstList[first][1] > secondList[second][1]:
                second+=1
            else:
                first+=1
                second+=1

            if curr[0] <= curr[1]:
                output.append(curr)

        return output
