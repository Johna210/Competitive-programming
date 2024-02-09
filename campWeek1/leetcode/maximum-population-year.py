class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        min_year = min(logs,key=lambda a: a[0])[0]
        max_year = max(logs,key=lambda a: a[1])[1]
        n = max_year - min_year + 1
        prefix = [0] * (n)
        
        for log in logs:
            prefix[log[0] - min_year] += 1
            if log[1] - min_year < n:
                prefix[log[1] - min_year] -= 1

        max_value = prefix[0]
        for i in range(1,n):
            prefix[i]+=prefix[i-1]
            max_value = max(max_value,prefix[i])
        
        for i in range(n):
            if prefix[i] == max_value:
                return min_year + i


