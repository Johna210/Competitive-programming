# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        left_pointer = right_pointer = dummy
        while n > 0:
            right_pointer = right_pointer.next
            n-=1
        
        while right_pointer and right_pointer.next:
            right_pointer = right_pointer.next
            left_pointer = left_pointer.next

        if left_pointer.next:
            left_pointer.next = left_pointer.next.next

        return dummy.next