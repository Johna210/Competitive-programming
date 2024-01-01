class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        output = []
        for i in range(len(arr),1,-1):
            max_val = max(arr[0:i])
            for j in range(i):
                if arr[j] == max_val:
                    output.append(j+1)
                    output.append(i)
                    break
            
            arr[0:j+1] = arr[j::-1]
            arr[0:i] = arr[i-1::-1]
            
        return output