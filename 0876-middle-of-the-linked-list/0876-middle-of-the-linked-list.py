# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        temp = head
        count = 0
        while temp!=None:
            temp = temp.next
            count+=1
        temp = head
        mid = count // 2
        
        count = 0
        while temp!=None:
            if count == mid:
                break
            temp = temp.next
            count+=1
        return temp
        