# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        first = head
        second = head.next
        
        while second:
            if second.val < first.val:
                new_ptr = dummy
                while second.val > new_ptr.next.val:
                    new_ptr = new_ptr.next
                first.next = second.next
                second.next = new_ptr.next
                new_ptr.next = second
                second = first.next
            else:
                first = first.next
                second = second.next

        return dummy.next

        