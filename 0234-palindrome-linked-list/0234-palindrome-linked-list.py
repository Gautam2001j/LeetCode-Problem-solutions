# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverse(self,node):
        if node==None or node.next==None:
            return node
        newnode = self.reverse(node.next)
        front = node.next
        front.next = node
        node.next = None
        return newnode
    
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        slow = head
        fast = head
        while fast.next!=None and fast.next.next!=None:
            slow = slow.next
            fast = fast.next.next
        newhead = self.reverse(slow.next)
        first = head
        second = newhead
        while second!=None:
            if first.val != second.val:
                self.reverse(newhead)
                return False
            first = first.next
            second = second.next
        self.reverse(newhead)
        return True