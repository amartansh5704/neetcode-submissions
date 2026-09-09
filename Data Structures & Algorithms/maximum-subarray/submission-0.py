class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        min_sum = 0
        max_sum = nums[0]
        rolling_sum = 0
        for n in nums:
            rolling_sum += n
            max_sum = max(max_sum, rolling_sum - min_sum)
            min_sum = min(min_sum, rolling_sum)
        return max_sum