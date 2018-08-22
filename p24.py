class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    #     def swapPairs(self, head):
    #         """
    #         :type head: ListNode
    #         :rtype: ListNode
    #         """
    #         if not head: return None
    #         if not head.next: return head

    #         cur = head
    #         pre = ListNode(0)
    #         dummy_head = pre
    #         while cur and cur.next:
    #             next = cur.next
    #             temp = next.next
    #             next.next = cur
    #             cur.next = temp
    #             pre.next = next
    #             pre = cur
    #             cur = cur.next
    #         return dummy_head.next

    def swapPairs(self, head):
        if not head or not head.next:
            return head

        next = head.next
        temp = next.next
        next.next = head
        head.next = self.swapPairs(temp)
        return next