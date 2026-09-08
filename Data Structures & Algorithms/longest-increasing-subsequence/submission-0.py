class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = defaultdict(int)

        for i in range(len(nums) -1, -1 , -1):
            dp[-1] = max(dp[-1], dp[i] + 1)

            for j in range(i):
                if nums[j] < nums[i]:
                    dp[j] = max(dp[j], dp[i]+1)
        return dp[-1]