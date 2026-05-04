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
        if head==None or head.next==None:
            return None
        count = 0
        temp = head
        while temp!=None:
            count += 1
            temp = temp.next
        if n == count:
            return head.next
        deletenode = count - n
        temp = head
        while temp!=None:
            deletenode -= 1
            if deletenode <= 0:
                break
            temp = temp.next
        print(temp)
        delnode = temp.next
        temp.next = delnode.next
        delnode = None

        return head