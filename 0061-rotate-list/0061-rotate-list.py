# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def findnthNode(self, temp, d):
        cnt = 1
        while temp!=None:
            if cnt==d:
                return temp
            cnt+=1
            temp = temp.next
        return temp

    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return None
        Len = 1
        tail = head

        while tail.next!=None:
            Len += 1
            tail = tail.next
        
        if k%Len == 0:
            return head
        k = k%Len

        tail.next = head
        newtail = self.findnthNode(head,Len-k)
        head = newtail.next
        newtail.next = None

        return head