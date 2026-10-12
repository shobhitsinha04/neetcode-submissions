class Solution:
    def trap(self, height: List[int]) -> int:
        # water depends on the lowest bar around and the
        # amt of water is maxwall on that side - len(bar)
        # if not height:
        #     return 0
        # l = 0
        # r = len(height) - 1
        # maxL = height[l]
        # maxR = height[r]

        # res = 0
        # while l < r:
        #     if maxL < maxR:
        #         l += 1
        #         maxL = max(maxL, height[l])
        #         res += maxL - height[l]
        #     else:
        #         r -= 1
        #         maxR = max(maxR, height[r])
        #         res += maxR - height[r]
        # return res
        if not height:
            return 0
        left = 0
        right = len(height) - 1
        left_max = height[left]
        right_max = height[right]
        water = 0

        while left < right:
            if left_max <= right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]
        return water

