"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        days = 0 
        starts = sorted(intervals, key = lambda x :  x.start )
        ends = sorted(intervals, key = lambda x: x.end)

        end_i = 0 
        for s in starts:
            if s.start < ends[end_i].end:
                days += 1
            else:
                end_i += 1
        return days