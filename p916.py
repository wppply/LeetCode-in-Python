class Solution:
    def wordSubsets(self, A, B):
        """
        :type A: List[str]
        :type B: List[str]
        :rtype: List[str]
        """
        res = []
        for word in A:
            flag = 1
            for ch in B:
                if ch not in A:
                    flag = 0
                    break
            if flag:
                res.append(word)

        return res

if __name__ == "__main__":
    s = Solution()
    b = s.wordSubsets(["amazon","apple","facebook","google","leetcode"], ['e', 'o'])
    print(b)