import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = [-1*num for num in nums]
        heapq.heapify(nums)

        for i in range(k):
            temp = heapq.heappop(nums)
        return -1 * temp


if __name__ == "__main__":
    s = Solution()
    nums = [84,2,7,21,53,6,4,1]
    k = 4
    res = s.findKthLargest(nums, k)

    print(res)
    print(res == sorted(nums)[k])
