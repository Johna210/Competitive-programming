class OrderedStream:

    def __init__(self, n: int):
        self.data = [0] * n
        self.pointer = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        self.data[idKey-1] = value
        output = []

        for i in range(self.pointer,len(self.data)):
            if self.data[i] == 0:
                break
            output.append(self.data[i])
        self.pointer = i
        
        return output
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)