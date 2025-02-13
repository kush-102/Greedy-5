class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # tabulation method time complexity is O(m*n) and space complexity is O(m*n)
        m = len(s)
        n = len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = True

        for j in range(1, n + 1):
            pChar = p[j - 1]
            if pChar == "*":
                dp[0][j] = dp[0][j - 1]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pChar = p[j - 1]
                if pChar == "*":
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                elif pChar == s[i - 1] or pChar == "?":
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = False

        return dp[m][n]

        # time complexity is O(m*n)
        # using recusrion with memoization
        dp = {}

        def helper(i, j):
            # If (i, j) already computed, return from memo
            if (i, j) in dp:
                return dp[(i, j)]

            # Base cases
            if i == len(s) and j == len(p):
                return True
            if j == len(p):
                return i == len(s)
            if i == len(s):
                return all(char == "*" for char in p[j:])

            # Match cases
            if s[i] == p[j] or p[j] == "?":
                dp[(i, j)] = helper(i + 1, j + 1)
            elif p[j] == "*":
                # '*' can match empty (skip '*') OR match one character and continue
                dp[(i, j)] = helper(i + 1, j) or helper(i, j + 1)
            else:
                dp[(i, j)] = False

            return dp[(i, j)]

        return helper(0, 0)
        # time complexity is O(m*n)
        # space complexity is O(m*n)
