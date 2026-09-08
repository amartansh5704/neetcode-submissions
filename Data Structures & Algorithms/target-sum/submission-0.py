class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp_i1 = defaultdict(int)
        dp_i1[0] = 1

        for i in range(len(nums) -1, -1, -1):
            dp_i = defaultdict(int)
            for t, ways in dp_i1.items():
                dp_i[t + nums[i]] += ways
                dp_i[t - nums[i]] += ways
            dp_i1 = dp_i
        return dp_i1[target]