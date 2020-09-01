# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr1 = head
        
        while curr1 != None:
            curr2 = curr1.next
            while curr2 != None and curr2.val == curr1.val:
                curr1.next = curr2.next
                curr2 = curr2.next
            curr1 = curr1.next
        
        return head
