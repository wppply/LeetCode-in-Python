class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        def dfs(sol, i, j, level):
            if level > len(word):
                return False
            if sol == word:
                return True

            res = False
            if 0 <= i < len(board) and 0 <= j < len(board[0]) and board[i][j] != '#':
                letter = board[i][j]
                board[i][j] = '#'
                res = dfs(sol + letter, i - 1, j, level + 1) or \
                      dfs(sol + letter, i + 1, j, level + 1) or \
                      dfs(sol + letter, i, j - 1, level + 1) or \
                      dfs(sol + letter, i, j + 1, level + 1)
                board[i][j] = letter
            return res

        return bool(sum([dfs('', i, j, 0) for i in range(len(board)) for j in range(len(board[0]))]))
