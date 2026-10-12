class Solution:
    def rob(self, nums: List[int]) -> int:
        prev1 = 0
        prev2 = 0
        for money in nums:
            take = prev2 + money
            skip = prev1
            temp = max(take,skip)
            prev2 = prev1
            prev1 = temp
        return prev1
