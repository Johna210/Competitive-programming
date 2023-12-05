class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:    
        if start > destination:
            start,destination = destination,start
        i = start
        difference = 0
        while i < destination:
            difference += (distance[i])
            i+=1
            if i == destination:
                break
        return min(difference,sum(distance[i:])+sum(distance[0:start])) 