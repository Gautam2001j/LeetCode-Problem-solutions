# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        Map = dict()
        temp = head
        while temp!=None:
            if temp.val in Map:
                Map[temp.val] += 1
            else:
                Map[temp.val] = 1
            temp = temp.next
        
        temp = head
        prev = ListNode(-1)
        res = prev
        while temp!=None:
            if Map[temp.val]>1:
                front = temp.next
                prev.next = front
                temp = front
            else:
                prev.next = temp
                prev = temp
                temp = temp.next
        return res.next