# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        if not prev:
            return head
        ahead = prev.next

        while ahead:
            while prev and ahead and prev.val == ahead.val:
                prev.next = ahead.next
                ahead = ahead.next                
                
            
            prev = prev.next
            if ahead:
                ahead = ahead.next
                
        return head