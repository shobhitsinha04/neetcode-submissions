class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # what is being done is that the window is going to keep the 
        # longest substring so you move r normally but you move l when old char comes
        l = 0 
        r = len(s) - 1
        res = 0 
        charset = set()
        for r in range(len(s)):
            while s[r] in charset:
                charset.remove(s[l])
                l += 1
            charset.add(s[r])
            res = max(res, r-l+1)
        return res
