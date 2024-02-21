# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        length = 0
        curr = head
        lst = []
        while curr:
            length+=1
            curr = curr.next
        part = length // k
        left = length%k
        if length < k:
            while head:
                lst.append(ListNode(head.val))
                head = head.next
                k-=1
            while k:
                lst.append(head)
                k-=1
        else:
            dummy = ListNode()
            dummy2 = ListNode()
            dummy2.next = dummy
            l = part
            r = left
            while head:
                if l:
                    node = ListNode(head.val)
                    dummy.next = node
                    dummy = dummy.next
                    l-=1
                    head = head.next

                elif not l and r:
                    left-=1
                    r=0
                    node = ListNode(head.val)
                    dummy.next = node
                    head = head.next
                else:
                    lst.append(dummy2.next.next)
                    l = part
                    r = left
                    dummy = ListNode(head.val)
                    dummy2 = ListNode()
                    dummy2.next = dummy
            if dummy2:
                lst.append(dummy2.next.next)
        return lst