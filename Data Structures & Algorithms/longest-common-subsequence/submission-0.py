class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [0] * (len(text2) + 1)

        # loop over characters of text1
        for i in range(1, len(text1) + 1):
            # store dp[j-1] from the previous row
            prev_diag = 0

            # loop over characters of text2
            for j in range(1, len(text2) + 1):
                # save old dp[j] before overwrite
                up = dp[j]

                # if current characters match
                if text1[i - 1] == text2[j - 1]:
                    # take diagonal and add 1
                    dp[j] = prev_diag + 1
                else:
                    # take the best of skipping from top or left
                    dp[j] = max(dp[j], dp[j - 1])

                # move diagonal for next column
                prev_diag = up

        # dp[-1] is the answer for full strings
        return dp[-1]