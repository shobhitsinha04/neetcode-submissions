class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
            l = i + 1
            r = n - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
        return res



        # # so the way to approach this is
        # # use a hash map as we need information about the nums
        # # what we will do is unlike two sum we will find 2 unique values and then find the 
        # # third value by using third = - ( first + second) as they all have to sum up to 0 
        # res = []
        # nums.sort()
        # count = defaultdict(int)
        # for num in nums:
        #     count[num] += 1

        # # finding the first element
        # for i in range(len(nums)):
        #     count[nums[i]] -= 1 # to make sure it doesnt get repeated
        #     if i != 0 and nums[i] == nums[i-1]:
        #         continue
            
        #     # now finding j 
        #     for j in range(i+1, len(nums)):
        #         count[nums[j]] -= 1
        #         if j-1>i and nums[j] == nums[j-1]:
        #             continue
        #         target = - (nums[i] + nums[j])
        #         if count[target] > 0:
        #             res.append([nums[i], nums[j], target])
            
        #     # then updating j back for the other i's
        #     for j in range(i+1, len(nums)):
        #         count[nums[j]] += 1
        
