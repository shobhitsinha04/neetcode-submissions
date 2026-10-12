class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res = []
        for x in nums:
            l, r = 0, len(res)
            while l<r:
                m = (l+r)//2
                if res[m] < x:
                    l = m+1
                else:
                    r = m
            if l == len(res):
                res.append(x)
            else:
                res[l] = x
        return len(res)