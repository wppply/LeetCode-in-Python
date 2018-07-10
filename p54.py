class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        while matrix:
	        for row in matrix.pop(0):
	        	if type(row) is int: 
	        		res.append(row)
	        	else:
	        		res += row

        	matrix = zip(*matrix)[::-1]
        return res