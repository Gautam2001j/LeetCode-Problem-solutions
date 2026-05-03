# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        count = 0
        temp = head
        while temp!=None:
            count += 1
            temp = temp.next
        mid = count//2
        temp = head
        prev = None
        while temp!= None:
            if mid == 0:
                break
            mid = mid-1
            prev = temp
            temp = temp.next
        if prev==None:
            return
        prev.next = temp.next
        temp.next = None

        return head

