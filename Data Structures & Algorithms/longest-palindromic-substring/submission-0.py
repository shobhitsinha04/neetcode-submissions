class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        best_l = 0 
        best_r = 0
        def expand(l, r):
            while l>= 0 and r< len(s) and s[l]==s[r]:
                l-=1
                r+=1 
            return l+1, r-1
        for i in range(len(s)):
            l1,r1 = expand(i,i) #odd length
            l2,r2 = expand(i, i+1) #even length
            if r1-l1 > best_r - best_l:
                best_r, best_l = r1,l1
            if r2-l2 > best_r - best_l:
                best_r, best_l = r2,l2
        return s[best_l: best_r+1]