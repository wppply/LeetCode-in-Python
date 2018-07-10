# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return head


        count = 1
        dummyhead = head
        while head.next:
        	head = head.next
        	count += 1
        # head become the tail after loop
        pre = head
        head.next = dummyhead # circular list
        head = dummyhead
        res = k % count

        while res:
        	pre = pre.next
        	head = head.next
        	res -= 1 
        pre.next = None
        return head
