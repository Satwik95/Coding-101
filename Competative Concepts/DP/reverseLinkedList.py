# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        cur  = head
        
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
            
        head = prev
        return head