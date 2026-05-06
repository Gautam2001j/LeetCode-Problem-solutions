# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):

    def findmiddle(self,head):
        slow = head
        fast = head.next
        while fast!=None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
        return slow

    def mergeTwoLists(self, list1, list2):
        t1 = list1
        t2 = list2
        dummynode = ListNode(-1)
        temp = dummynode

        while t1!=None and t2!=None:
            if t1.val<=t2.val:
                temp.next = t1
                temp = t1
                t1 = t1.next
            else:
                temp.next = t2
                temp = t2
                t2 = t2.next
        
        if t1:
            temp.next = t1
        else:
            temp.next = t2
        
        return dummynode.next 

    def sortList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head
        middle = self.findmiddle(head)
        lefthead = head
        righthead = middle.next
        middle.next = None
        lefthead = self.sortList(lefthead)
        righthead = self.sortList(righthead)

        return self.mergeTwoLists(lefthead,righthead)