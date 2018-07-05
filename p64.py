class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        col,row = len(grid[0]),len(grid)
        res = [[0]*col]*row

        for i in range(0,row):
        	for j in range(0,col):
        		if not i and not j:
        			res[i][j] = grid[i][j]
        		elif not i: # first row
        			res[i][j] = res[i][j-1] + grid[i][j]
        		elif not j: # first col
        			res[i][j] = res[i-1][j] + grid[i][j]
        		else:
        			res[i][j] = min(res[i-1][j],res[i][j-1]) + grid[i][j]
        print(res)
        return res[-1][-1]
    # save more space
    # def minPathSum(self, grid):
    #     m = len(grid)
    #     n = len(grid[0])
    #     for i in range(1, n):
    #         grid[0][i] += grid[0][i-1]
    #     for i in range(1, m):
    #         grid[i][0] += grid[i-1][0]
    #     for i in range(1, m):
    #         for j in range(1, n):
    #             grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    #     return grid[-1][-1]

if __name__ == '__main__':
    s = Solution()
    grid = [[1,1,1],[1,1,1],[1,1,1]]
    print(s.minPathSum(grid))

