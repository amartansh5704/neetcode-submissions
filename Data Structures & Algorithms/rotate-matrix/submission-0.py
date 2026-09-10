class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        import numpy as np

        arr = np.array(matrix)
        transposed = arr.T

        reversed = [row[::-1] for row in transposed]

        for i in range(len(matrix)):
            matrix[i] = reversed[i].tolist()