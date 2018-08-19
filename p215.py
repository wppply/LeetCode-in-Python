import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        h = heapq.heapify(nums)

        for i in range(k):
            temp = heapq.heappop(h)
        return temp