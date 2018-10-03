
def maximalRectangle(matrix):
    """
    :type matrix: List[List[str]]
    :rtype: int
    """
    m, n = len(matrix), len(matrix[0])
    res = 0
    dp = [[(0, 0) for _ in range(n+1)] for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if matrix[i-1][j-1] == '1':
                # case 1 matrix:
                temp_h, temp_w = min(dp[i - 1][j - 1][0], dp[i - 1][j][0]) + 1, min(dp[i - 1][j - 1][1],
                                                                                    dp[i][j - 1][1]) + 1
                # case 2.1 vector:
                if temp_h * temp_w <= dp[i - 1][j][0] + 1:
                    temp_h, temp_w = dp[i - 1][j][0] + 1, 1
                    # case 2.2
                if temp_h * temp_w <= dp[i][j - 1][1] + 1:
                    temp_h, temp_w = 1, dp[i][j - 1][1] + 1

                dp[i][j] = (temp_h, temp_w)
                res = max(res, dp[i][j][0] * dp[i][j][1])
    return res

a= [["0","0","0","1","0","1","0"],["0","1","0","0","0","0","0"],["0","1","0","1","0","0","1"],["0","0","1","1","0","0","1"],["1","1","1","1","1","1","0"],["1","0","0","1","0","1","1"],["0","1","0","0","1","0","1"],["1","1","0","1","1","1","0"],["1","0","1","0","1","0","1"],["1","1","1","0","0","0","0"]]
b = maximalRectangle(a)
print(b)