from bisect import bisect_left, bisect_right
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        left = bisect_left(intervals, newInterval[0], key = lambda x: x[1])
        right = bisect_right(intervals, newInterval[1], key = lambda x: x[0])
        if left < right:
            newInterval[0] = min(newInterval[0], intervals[left][0])
            newInterval[1] = max(newInterval[1], intervals[right - 1][1])
        intervals[left:right] = [newInterval]
        return intervals
        