# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        last = head
        while fast and fast.next:
            last = slow
            slow = slow.next
            fast = fast.next.next
        if fast == slow:
            return    
        
        last.next = None
        pre = None
        while slow:
            temp = slow.next
            slow.next = pre
            pre = slow
            slow = temp
       
        
        last = head
        while head:
            temp = head.next
            head.next = pre
            
            temp_pre = pre.next
            pre.next = temp
            head = temp
            last = pre
            pre = temp_pre
        
        if pre:
            last.next = pre
        
