class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        output = []
        count = 0
        ones = 0
        reverse_count = 0
        reverse_ones = 0
        dict_values = {}

        for j in range(len(boxes)):
            dict_values[j] = boxes[j]
            
            if dict_values[j] == "1":
                count+=j
                ones+=1
                reverse_count += (len(boxes) - 1 - j)
        reverse_ones = ones

        for val in dict_values:
            if dict_values[val] == "1":
                ones-=1
            output.append(count)
            count-=ones
        for i in range(len(boxes)-1,-1,-1):
            if reverse_count <= 0:
                break
            output[i] += reverse_count

            if dict_values[i] == "1":
                reverse_ones -= 1
            reverse_count-=reverse_ones
        
        return output


                

