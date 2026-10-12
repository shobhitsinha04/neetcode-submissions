class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in h_map:
                return [h_map[diff], i]
            h_map[val] = i


        h_map = {}
        for i, val in enumerate(nums):
            diff = target - val
            if diff in h_map:
                return [h_map[diff], i]
            h_map[val] = i