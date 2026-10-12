class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # using hash set for quick lookup
        numset = set(nums)
        counter = 0 
        for num in numset:
            if num-1 not in numset:
                length = 1 
                while num+length in numset:
                    length += 1
                counter = max(length, counter)
        
        return counter