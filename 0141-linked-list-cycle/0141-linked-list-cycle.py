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
        Set = set()
        temp = head
        while temp!=None:
            if temp in Set:
                return True
            Set.add(temp)
            temp = temp.next
        return False