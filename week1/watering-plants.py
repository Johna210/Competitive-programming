class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0

        can = capacity

        for i in range(len(plants)):
            if can - plants[i] >= 0:
                steps += 1
                can -= plants[i]
            else:
                can = capacity
                steps += i
                steps += (i + 1)
                can -= plants[i]  

        return steps