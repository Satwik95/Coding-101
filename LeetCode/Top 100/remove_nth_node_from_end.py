# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return 
        
        first = second = head
        count = 0
        
        while second and count<n:
            second = second.next
            if not second:
                return head.next
            count += 1
        
        while second and second.next:
            first = first.next
            second = second.next
        
        first.next = first.next.next
            
        return head      
        