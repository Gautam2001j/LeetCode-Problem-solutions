# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        Map = set()
        temp = head
        while temp!=None:
            if temp in Map:
                return temp
            Map.add(temp)
            temp=temp.next
        return None