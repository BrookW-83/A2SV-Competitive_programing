class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        res = [0] * (100 + 1)

        for b, d in logs:
            b -= 1950
            d -= 1950

            res[b] += 1
            res[d] -= 1

        for i in range(1, 100):
            res[i] += res[i - 1]

        i = max(res)

        return res.index(i) + 1950
        