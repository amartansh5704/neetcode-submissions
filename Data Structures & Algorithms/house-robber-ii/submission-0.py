class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return nums[0]

        taken_taken = float('-inf')
        taken_skipped = nums[0]
        skipped_taken = nums[1]
        skipped_skipped = 0

        for i in range(2, len(nums)):
            ( taken_taken, taken_skipped, skipped_taken, skipped_skipped) = ( taken_skipped + nums[i], max(taken_taken, taken_skipped), skipped_skipped + nums[i], max(skipped_skipped, skipped_taken))

        return max(taken_skipped, skipped_taken, skipped_skipped)
        