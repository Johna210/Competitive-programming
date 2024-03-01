# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less, greater = ListNode(0), ListNode(0)
        
        less_curr, greater_curr = less, greater
        
        while head:
            if head.val < x:
                less_curr.next, less_curr = head, head
            else:
                greater_curr.next, greater_curr = head, head
            
            head = head.next
        
        greater_curr.next = None
        
        less_curr.next = greater.next
        
        return less.next

        
       
