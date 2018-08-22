class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n: return []
        output = []

        def dfs(l, r, sol):
            if l + r == 2 * n:
                output.append(sol)
                return
            if l < n:
                dfs(l+1, r, sol+'(')
            if r < l:
                dfs(l, r+1, sol+')')
        dfs(0, 0, '')

        return output