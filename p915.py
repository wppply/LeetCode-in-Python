class Solution:
    def partitionDisjoint(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left = [A[0]] * len(A)  # large include i
        right = [A[-1]] * len(A)  # small include i

        for i in range(1, len(A)):
            left[i] = max(left[i-1], A[i])
        for i in range(len(A) - 2, -1, -1):
            right[i] = min(right[i + 1], A[i])
        for i in range(1, len(A)):
            if left[i - 1] <= right[i]:
                return i
        return 0
if __name__ == "__main__":
    s = Solution()
    b = s.partitionDisjoint([1,1,1,0,6,12])
    print(b)