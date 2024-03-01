# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        last = ListNode()
        def reverse(node):
            if not node:
                return
            if not node.next:
                last.next = node
                return node
            curr = reverse(node.next)
            node.next = None
            curr.next = node
            return node
       
        dummy = ListNode(0,head)
        pointer1, pointer2 = dummy, head

        # To find the starting point of the list to be reversed
        for _ in range(left-1):
            pointer1, pointer2 = pointer2, pointer2.next
        pointer1.next = None

        # To find the end point of the list to be reversed
        right_side = pointer2
        for _ in range(right-left):
            right_side = right_side.next
        last_part = right_side.next
        right_side.next = None

        # Joining the left part, The part to be reversed and the right part
        # The left_part is stored in variable last in the above function
        output = reverse(pointer2)
        pointer1.next = last.next
        output.next = last_part

        return dummy.next