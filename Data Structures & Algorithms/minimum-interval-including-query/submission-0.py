class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        heap = []
        hmap = {}
        i = 0
        for q in sorted(queries):
            while i in range(0, len(intervals)) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(heap, (r-l + 1, r))
                i += 1

            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            hmap[q] = heap[0][0] if heap else -1
        return [hmap[q] for q in queries]