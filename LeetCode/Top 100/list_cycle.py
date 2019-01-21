# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        while fast and not fast.next is None:
            slow = slow.next
            fast = fast.next.next
            if slow==fast:
                break
        if fast is None or fast.next is None:
            return False
        
        #slow=head
        #while slow!=fast:
         #   slow = slow.next
          #  fast = fast.next
        
        return True
