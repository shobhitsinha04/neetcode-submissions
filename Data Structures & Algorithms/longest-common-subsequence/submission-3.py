class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * (len(text2) + 1)
        for i in range(1, len(text1)+1):
            prev_diag = 0 

            for j in range(1, len(text2)+1):
                up = dp[j]
                if text1[i-1] == text2[j-1]:
                    dp[j] = prev_diag + 1
                else:
                    dp[j] = max(dp[j], dp[j-1])
                prev_diag = up
        return dp[-1]
