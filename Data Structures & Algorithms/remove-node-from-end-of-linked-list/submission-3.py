# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        n_node = head
        
        while n > 1:
            n_node = n_node.next
            n-=1
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while n_node and n_node.next:
            prev = head
            head = head.next
            n_node = n_node.next
        
        temp = head.next
        prev.next = temp
        
        return dummy.next
        
        
