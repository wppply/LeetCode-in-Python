def generate(self, numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """
    if not numRows:
        return []
    
    res = [[1]]
    for i in range(1, numRows):
        res.append([0] * (i + 1))
        for j in range(i + 1):
            if j == 0 or j == i:
                res[i][j] = 1
            else:
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j]
    return res