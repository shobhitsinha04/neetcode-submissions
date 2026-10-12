class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # needed prefix sum = current sum - goal
        count = {0:1} # empty prefix has sum 0
        current_sum = 0
        result = 0
        for num in nums:
            current_sum += num
            # counting earlier prefix that give our goal
            needed = current_sum - goal
            result += count.get(needed, 0)

            # store the current prefix sum
            count[current_sum] = count.get(current_sum, 0) + 1
        return result