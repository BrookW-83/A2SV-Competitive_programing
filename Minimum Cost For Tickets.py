class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0 for _ in range(366)]
        days = set(days)

        for i in range(1, len(dp)):
            if i in days:
                dp[i] = min(dp[i - 1] + costs[0], dp[i - 7]+costs[1], dp[i-30]+costs[2])
            else:
                dp[i] =dp[i-1]


        return dp[-1]
