class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums) - 1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        pivot = l 

        def search(l,r,nums,target):
            if l > r: return -1
            m = l + (r-l)//2
            if nums[m] < target:
                return search(m+1, r, nums, target)
            elif nums[m] > target:
                return search(l,m-1,nums, target)
            else:
                return m


        result = search(0, pivot-1, nums, target)
        if result != -1:
            return result
        return search(pivot, len(nums)-1, nums, target)