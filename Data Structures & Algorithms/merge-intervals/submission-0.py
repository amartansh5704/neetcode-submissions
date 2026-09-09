class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []

        i = 0
        while i <= len(intervals) - 1:
            start, end = intervals[i]

            while i + 1 <= len(intervals) - 1 and intervals[i+1][0] <= end:
                s, e = intervals[i+1]
                end = max(end, e)
                i = i+1

            res.append([start, end])
            i = i+1
        return res