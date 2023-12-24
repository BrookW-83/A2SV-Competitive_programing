class Solution:
    def __init__(self):
        self.soupA = [100, 75, 50, 25]
        self.soupB = [0, 25, 50, 75]

    def helper(self, a, b, dp):
        if a == 0 and b == 0:
            return 0.5

        if a == 0:
            return 1
        if b == 0:
            return 0

        if dp[a][b] != -1:
            return dp[a][b]

        res = 0
        for i in range(4):
            optionA = a - self.soupA[i]
            optionB = b - self.soupB[i]

            res += 0.25 * self.helper(max(0, optionA), max(0, optionB), dp)

        dp[a][b] = res
        return res

    def soupServings(self, n: int) -> float:
        if n >= 4800:
            return 1

        dp = [[-1] * (n+1) for _ in range(n + 1)]
        return self.helper(n, n, dp)
        