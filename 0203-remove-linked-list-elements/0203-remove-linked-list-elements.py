# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        
        temp = head
        prev = ListNode(-1)
        res = prev
        while temp != None:
            if temp.val == val:
                prev.next = temp.next
                temp = temp.next
            else:
                prev.next = temp
                prev = temp
                temp = temp.next
        return res.next