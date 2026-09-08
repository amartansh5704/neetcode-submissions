from collections import defaultdict
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dic = {}

        def dfs(i, curr_sum):
            if curr_sum == amount:
                return 1

            if curr_sum > amount or i == len(coins):
                return 0

            if (i, curr_sum) in dic:
                return dic[(i, curr_sum)]

            use = dfs(i, curr_sum + coins[i])

            skip = dfs(i+1, curr_sum)

            dic[(i, curr_sum)] = use + skip
            return dic[(i, curr_sum)]
        return dfs(0,0)   