class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        min_diff = float('inf')
        best = 0
        for k in range(len(nums)):
        	tempTarget = target - nums[k]

        	i, j = k+1, len(nums)-1
        	while i < j:
        		s = nums[k] + nums[i] + nums[j]
        		diff = s - target
        		if abs(diff) < min_diff:
        			min_diff = abs(diff)
        			best = s
        		if diff == 0:
        			return target
        		if diff > 0:
        			j -= 1
        		else:
        			i += 1
        return best

if __name__ == "__main__":
	sol = Solution()
	nums = [1,3,4,51,123,12,34,53,21,2,57]
	target = 100
	print(sol.threeSumClosest(nums,target))




