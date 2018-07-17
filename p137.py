class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(32):
        	bit_sum = 0
        	for num in nums:
        		bit_sum += (num >> i)&1
        	# because there are only 3 count and 1 count in array
        	ans |= (bit_sum%3) << i 
        return self.convert(ans)

    def convert(self,x):
        # bit operation follows signed int 
        # but python int has no upper bound b/c it is obj
        if x >= 2**31:
            x -= 2**32
        return x