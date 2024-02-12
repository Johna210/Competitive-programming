# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = ListNode()
        dummy = ListNode(0,merged_list)

        while list1 and list2:
            if list1.val < list2.val:
                merged_list.next = list1
                merged_list = merged_list.next
                list1 = list1.next
            else:
                merged_list.next = list2
                merged_list = merged_list.next
                list2 = list2.next

        while list1:
            merged_list.next = list1
            list1 = list1.next
            merged_list = merged_list.next

        while list2:
            merged_list.next = list2
            list2 = list2.next
            merged_list = merged_list.next

        return dummy.next.next