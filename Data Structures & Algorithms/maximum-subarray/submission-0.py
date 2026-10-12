class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        best = nums[0]
        for i in range(1, len(nums)):
            x = nums[i]
            curr = max(x, curr+x)
            best = max(best, curr)
        return best