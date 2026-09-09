class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_farthest = 0
        farthest = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_farthest:
                jumps += 1
                current_farthest = farthest

        return jumps