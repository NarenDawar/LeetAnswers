"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key= lambda i : i.start)
        for i in range(len(intervals)-1):
            curr = intervals[i]
            nxt = intervals[i + 1]
            if (nxt.start < curr.end):
                return False
        return True

#video solution: https://youtu.be/Qd0o2KnTMKA            
