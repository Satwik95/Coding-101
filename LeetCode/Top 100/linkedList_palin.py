# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        slow = fast = head
        temp = head
        count = 0
        
        while temp:
            count +=1
            temp = temp.next
            
        if count==1:
            return True
        
        prev = None
        while fast and fast.next:
            cur = slow                        
            slow = slow.next
            fast = fast.next.next
            cur.next = prev
            prev = cur
            
        if count%2!=0:
            slow = slow.next
            
        temp = cur
        while temp and slow:
            if temp.val!=slow.val:
                return False
            slow = slow.next
            temp = temp.next
        return True
        