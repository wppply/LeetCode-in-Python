class Solution(object):
    def divide(self, dividend, divisor):
        """
        initial Guess with most straight forward thought
        TIME OUT
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        b, a = abs(divisor), abs(dividend)
        sign_b = 1 if divisor>=0 else -1
        sign_a = 1 if dividend>=0 else -1
        if b == 0 : return 2**31 - 1
        res = 0
        while a >= b:
        	a -= b
        	res += 1
        
        return res if sign_a == sign_b else -res


class Solution(object):
    def divide(self, dividend, divisor):
        """
        Use the thought of "slow start" in Networt
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        sign = (dividend < 0) == (divisor < 0)
        dividend, divisor = abs(dividend),abs(divisor)

        if divisor == 0: return 2**31-1 if sign else -2**31

        res = 0
        while dividend >= divisor:
        	temp, i = divisor, 1
        	while dividend >= temp:
        		dividend -= temp
        		res += i
        		i <<= 1
        		temp <<= 1
        if not sign:
        	res = 0 - res
        return min(max(-2147483648, res), 2147483647)

S = Solution()
print(S.divide(10,-3))