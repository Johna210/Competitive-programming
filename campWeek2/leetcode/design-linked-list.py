class Node:
    def __init__(self,value = 0):
        self.value = value
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = Node()
        self.size = 0
    
    def get_node(self,index):
        curr = self.head

        while curr and index >= 0:
            curr = curr.next
            index-=1
        
        return curr

    def get(self, index: int) -> int:
        if index < self.size:
            node = self.get_node(index)
            if node:
                return node.value
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val)
        temp = self.head.next
        self.head.next = node
        node.next = temp
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        curr = self.head

        while curr.next:
            curr = curr.next
        
        curr.next = node
        self.size+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= self.size:
            node = Node(val)
            curr = self.head
            while index>0:
                curr = curr.next
                index-=1

            node.next = curr.next
            curr.next = node
            self.size += 1


    def deleteAtIndex(self, index: int) -> None:
        if index < self.size:
            prev_node = self.get_node(index-1)
            curr_node = self.get_node(index)
            prev_node.next = curr_node.next
            self.size -= 1
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)