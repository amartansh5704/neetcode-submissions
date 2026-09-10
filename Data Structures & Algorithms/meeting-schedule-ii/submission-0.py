class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        events = sorted((t, d) for iv in intervals for t, d in ((iv.start, 1), (iv.end, -1)))
        return max(accumulate(d for _, d in events), default=0)