class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n : return []
        res = []
        self.helper(n,n, '', res)
        return res

    def helper(self,left,right, cur, res):
        if right < left:
	        return
        if not left and not right:
        	res.append(cur)
        	return
        if left :
        	# cur += '(' # this will result in some error
        	self.helper(left-1, right, cur+'(', res)
        if right:
	        # cur += ')' 
	        self.helper(left, right-1, cur+')', res)



if __name__ == '__main__':
	s = Solution()
	res = s.generateParenthesis(2)
	print(res)

