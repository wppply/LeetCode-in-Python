class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        if obstacleGrid[0][0] == 1: return 0
        for i in range(len(obstacleGrid)):
        	for j in range(len(obstacleGrid[0])):
        		if obstacleGrid[i][j] == 1 or i == j == 0:
        			obstacleGrid[i][j] -= 1
        		else:
        			a = obstacleGrid[i-1][j] if i > 0 else 0
        			b = obstacleGrid[i][j-1] if j > 0 else 0
        			obstacleGrid[i][j] += (a+b)
        return abs(obstacleGrid[-1][-1])