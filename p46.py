class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # if not nums: return []
        output = []

        def dfs(level, nums):
            # nums will be modified
            if level == len(nums):
                output.append(nums.copy())  # nums[:] for python 2
                return

            for i in range(level, len(nums)):
                nums[level], nums[i] = nums[i], nums[level]
                dfs(level + 1, nums)
                # !!!! exchange back
                nums[i], nums[level] = nums[level], nums[i]

        dfs(0, nums)
        return output


if __name__ == '__main__':
    s = Solution()
    res = s.permute([1, 2, 3])
    print(res)