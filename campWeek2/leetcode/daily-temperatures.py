class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        values = {}
        stack = []
        output = [0] * len(temperatures)
        lst = []
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                values[stack.pop()] = i
            
            stack.append(i)

        for i in values:
            output[i] = (values[i] - i)

        return output