class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return True
        r = len(strs[0])
        for s in strs[1:]:
            while r > 0 and strs[0][:r] != s[:r]:
                r -= 1
            if r == 0:
                return ""
        return strs[0][:r]