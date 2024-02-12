# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first_pointer = second_pointer = head
        
        while second_pointer and second_pointer.next:
            second_pointer = second_pointer.next.next
            first_pointer = first_pointer.next

        return first_pointer