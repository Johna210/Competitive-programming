class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        left = points[0]
        arrows = 1
        for i in range(1,len(points)):
            left = [max(left[0],points[i][0]),min(left[1],points[i][1])]
            if left[0] > left[1]:
                left = points[i]
                arrows+=1

        return arrows