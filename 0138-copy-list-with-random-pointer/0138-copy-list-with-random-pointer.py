"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return
        #create copy of nodes
        temp = head

        while temp!=None:
            copynode = Node(temp.val)
            copynode.next = temp.next
            temp.next = copynode
            temp = temp.next.next
        #connect random pointers
        temp = head
        while temp!=None:
            copynode = temp.next
            copynode.random = temp.random.next if temp.random else None
            temp = temp.next.next

        dummynode = Node(-1)
        res = dummynode
        temp = head

        while temp!=None:
            res.next = temp.next
            temp.next = temp.next.next
            res = res.next
            temp = temp.next

        return dummynode.next