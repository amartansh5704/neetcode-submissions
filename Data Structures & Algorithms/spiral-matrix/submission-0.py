class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # rip off the top row, and rotate the matrix each time
        res = []

        while not (len(matrix) == 1):
            # rip
            res.extend(matrix.pop(0))

            # rotate
            rotated = deque()
            for v in zip(*matrix):
                rotated.appendleft(list(v))
            matrix = list(rotated)

        # deal with the remainder
        res.extend(matrix[0])

        return res