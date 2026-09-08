from functools import cache
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        def do_search(i, j, last):
            if not (0 <= i < m and 0 <= j < n):
                return 0

            if matrix[i][j] >= last:
                return 0

            return search(i, j)

        @cache
        def search(i, j):
            value = matrix[i][j]
            return max(
                do_search(i - 1, j, value),
                do_search(i+ 1, j, value),
                do_search(i, j-1, value),
                do_search(i, j+1, value)
            ) + 1

        return max(search(i, j) for i, j in product(range(m), range(n)))