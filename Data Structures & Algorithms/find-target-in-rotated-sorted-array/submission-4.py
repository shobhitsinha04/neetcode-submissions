class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # first we need to find the pivot which is the smallest element and then just 
        # normal binary search 
        l = 0 
        r = len(nums) - 1

        # this is binary serach on minimum element
        while l < r:
            m = (l + r)//2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m 
        
        pivot = l

        def binary_search(left, right):
            while left<=right:
                mid = (left+right)//2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    return mid
            return -1

        result = binary_search(0,pivot-1)
        if result != -1:
            return result
        return binary_search(pivot, len(nums)-1)