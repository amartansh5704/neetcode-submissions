class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def conflicts(intervalA: List[int], intervalB: List[int]) -> bool:
            return (intervalA[0] <= intervalB[0] and intervalA[1] > intervalB[0]) or (intervalB[0] <= intervalA[0] and intervalB[1] > intervalA[0])

        intervals.sort()

        lastNonConflictingInterval = intervals[0]
        removals = 0

        for i in range(1, len(intervals)):
            nextInterval = intervals[i]

            if conflicts(lastNonConflictingInterval, nextInterval):
                lastNonConflictingInterval = lastNonConflictingInterval if lastNonConflictingInterval[1] < nextInterval[1] else nextInterval
                removals += 1
            else:
                lastNonConflictingInterval = nextInterval
        return removals