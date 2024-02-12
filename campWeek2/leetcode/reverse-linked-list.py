# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        right_side = head
        first = right_side
        left_side = None

        if not first:
            return head
        second = first.next

        while second:
            right_side = second.next
            second.next = first
            first.next = left_side
            left_side = first
            
            # Increment the right and left
            first = second
            second = right_side

        first.next = left_side
        left_side = first

        return left_side