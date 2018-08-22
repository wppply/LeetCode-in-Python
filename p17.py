class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if not digits: return []
        dial = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

        l = len(digits)
        output = []

        def dfs(level, sol):
            if level == l:
                output.append(sol)
                return

            choices = dial[digits[level]]
            for choice in choices:
                dfs(level + 1, sol + choice)

        dfs(0, '')

        return output


