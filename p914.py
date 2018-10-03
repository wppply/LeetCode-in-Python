from collections import Counter
class Solution(object):
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        if len(deck) < 2: return False
        d = Counter(deck)
        for X in range(2, len(deck)+1):
            temp_flag = 1
            for key, value in d.items():
                if value % X != 0:
                    temp_flag = 0
                    break
            if temp_flag: return True
        return False

if __name__ == "__main__":
    s = Solution()
    b = s.hasGroupsSizeX([1,1,2])
    print(b)