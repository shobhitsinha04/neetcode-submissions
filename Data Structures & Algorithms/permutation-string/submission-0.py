class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        need = [0] * 26
        window = [0] * 26
        m = len(s1)

        for i in range(m):
            need[ord(s1[i]) - ord("a")] += 1
            window[ord(s2[i]) - ord("a")] += 1
        
        if need == window:
            return True
        
        for r in range(m, len(s2)):
            window[ord(s2[r]) - ord("a")] += 1
            l = r - m
            window[ord(s2[l]) - ord("a")] -= 1
            if window == need:
                return True
        return False