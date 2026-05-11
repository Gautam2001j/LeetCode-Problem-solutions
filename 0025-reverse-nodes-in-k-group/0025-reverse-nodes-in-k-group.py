# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def findkthnode(self,temp,k):
        k -= 1
        while temp!=None and k>0:
            k-=1
            temp = temp.next
        return temp

    def reverse(self,temp):
        if temp==None or temp.next==None:
            return temp
        newhead = self.reverse(temp.next)
        front = temp.next
        front.next = temp
        temp.next = None
        return newhead

    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        temp = head
        prevnode = None
        nextnode = ListNode(-1)

        while temp!=None:
            kthnode = self.findkthnode(temp,k)
            if kthnode == None:
                if prevnode:
                    prevnode.next = temp
                break
            nextnode = kthnode.next
            kthnode.next = None
            self.reverse(temp)
            if temp == head:
                head = kthnode
            else:
                prevnode.next = kthnode
            
            prevnode = temp
            temp = nextnode
        return head
