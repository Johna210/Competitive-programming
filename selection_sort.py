class Solution: 
    def select(self, arr, i):
        smallest = i
        for j in range(i+1,len(arr)):
            if arr[j] <= arr[smallest]:
                smallest = j
        
        return smallest
            
    
    def selectionSort(self, arr,n):
        
        for i in range(n):
            value = self.select(arr,i)
            arr[i],arr[value] = arr[value],arr[i]
            
        return arr