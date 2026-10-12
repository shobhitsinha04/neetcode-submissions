from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_set = defaultdict(int)
        t_set = defaultdict(int)
        for i in range(len(s)):
            s_set[s[i]] += 1
            t_set[t[i]] += 1
        return s_set == t_set

