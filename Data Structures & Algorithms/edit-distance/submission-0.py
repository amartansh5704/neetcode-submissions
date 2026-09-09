class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        rows, cols = len(word2), len(word1)
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        for c in range(cols - 1, -1, -1):
            dp[rows][c] = dp[rows][c+1] +1
        for r in range(rows - 1, -1, -1):
            dp[r][cols] = dp[r + 1][cols] + 1
        

        for r in range(rows - 1, -1, -1):
            for c in range(cols -1 , -1, -1):
                if word1[c] == word2[r]:
                    dp[r][c] = dp[r+1][c+1]
                else:
                    dp[r][c] = 1+ min(dp[r+1][c+1], dp[r+1][c], dp[r][c+1])
        return dp[0][0]