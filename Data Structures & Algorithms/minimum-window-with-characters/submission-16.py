class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(t) > len(s):
            return ""
        
        need = Counter(t)
        window = defaultdict(int)

        required = len(need)
        formed = 0

        best_len = float("inf")
        best_l = 0
        l = 0 

        for r, c in enumerate(s):
            window[c] += 1
            if c in need and window[c] == need[c]:
                formed += 1
            while formed == required:
                curr_len = r - l + 1
                if curr_len < best_len:
                    best_len = curr_len
                    best_l = l
                window[s[l]] -= 1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    formed -= 1
                l += 1
        if best_len == float("inf"):
            return ""
        return s[best_l : best_l + best_len]