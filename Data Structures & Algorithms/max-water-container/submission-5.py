class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # l = 0 
        # r = len(heights) - 1
        # res = 0 
        # area = 0
        # while l < r:
        #     area = min(heights[l], heights[r]) * (r-l)
        #     res = max(area, res)
        #     if heights[l] < heights[r]:
        #         l += 1
        #     else:
        #         r -= 1
        # return res
        left = 0 
        right = len(heights) - 1
        res = 0 
        max_area = 0 
        while left < right:
            width = right - left
            height = min(heights[left], heights[right])
            max_area = max(max_area, width * height)
            # move the shorter bar inward
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area