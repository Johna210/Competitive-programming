# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.prev = None

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        prev_node = None
        right = head

        while right.next:
            right.prev = prev_node
            prev_node = right
            right = right.next
        right.prev = prev_node

        while head != right:
            if head.val != right.val:
                return False

            head = head.next
            right = right.prev

        return True