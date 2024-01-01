class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort()
        processorTime.sort()
        count = 0
        j = 0
        max_val = 0
        for i in range(len(tasks)-1,-1,-1):
            if count==4:
                count = 0
                j+=1

            if count < 4:
                max_val = max(max_val, processorTime[j] + tasks[i])
                count+=1
            
        return max_val