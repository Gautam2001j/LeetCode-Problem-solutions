# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if head is None:
            return None

        slow = head
        fast = head

        # Move fast n steps ahead
        for _ in range(n):
            fast = fast.next

        # If we need to delete head
        if fast is None:
            return head.next

        # Move both pointers
        while fast.next:
            slow = slow.next
            fast = fast.next

        # Delete node
        slow.next = slow.next.next

        return head