class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # so the way to approach this is
        # use a hash map as we need information about the nums
        # what we will do is unlike two sum we will find 2 unique values and then find the 
        # third value by using third = - ( first + second) as they all have to sum up to 0 
        res = []
        nums.sort()
        count = defaultdict(int)
        for num in nums:
            count[num] += 1

        # finding the first element
        for i in range(len(nums)):
            count[nums[i]] -= 1 # to make sure it doesnt get repeated
            if i != 0 and nums[i] == nums[i-1]:
                continue
            
            # now finding j 
            for j in range(i+1, len(nums)):
                count[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j-1]:
                    continue
                target = - (nums[i] + nums[j])
                if count[target] > 0:
                    res.append([nums[i], nums[j], target])
            
            # then updating j back for the other i's
            for j in range(i+1, len(nums)):
                count[nums[j]] += 1
        
        return res