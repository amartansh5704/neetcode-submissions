class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [10001] * (amount + 1)
        dp[0] = 0

        for curr in range(1, amount + 1):
            for coin in coins:
                if coin <= curr:
                    dp[curr] = min(dp[curr], dp[curr - coin] + 1)
        
        if dp[amount] == 10001:
            return -1

        return dp[amount]