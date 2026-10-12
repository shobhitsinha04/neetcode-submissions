class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {} # this is a hash map which will track the count of each char
        res = 0 
        l = 0 
        common = 0 
        # the size of the window is what we have to return 
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            common = max(common, count[s[r]])
        
            while r-l+1 - common > k:
                # this means still changes to make
                count[s[l]] -= 1
                l += 1
        res = max(res, r - l+ 1)
        return res