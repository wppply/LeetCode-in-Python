# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        out = []

        for i in sorted(Intervals , key=lambda i: i.start):
        	if out and i.start <= out[-1].end:
        		out[-1].end = max(out[-1].end,i.end)
        	else:
        		out.append(i)
        return out