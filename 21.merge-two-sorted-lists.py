# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    head = None
    res = None
    def set_next(self, val):
        if self.head == None:
            self.head = ListNode(val)
            self.res = self.head
        else:
            self.res.next = ListNode(val)
            self.res = self.res.next
    
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        curr1 = l1
        curr2 = l2
        self.head, self.res = None, None
        while curr1 != None and curr2 != None:
            if curr1.val < curr2.val:
                self.set_next(curr1.val)
                curr1 = curr1.next
            else:
                self.set_next(curr2.val)
                curr2 = curr2.next
                
        while curr1 != None:
            self.set_next(curr1.val)
            curr1 = curr1.next
        
        while curr2 != None:
            self.set_next(curr2.val)
            curr2 = curr2.next
            
        return self.head
            
