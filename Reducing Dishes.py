class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse = True)

        currSum, p , res = 0, 0, 0

        for i in range(len(satisfaction)):
            currSum += p + satisfaction[i]
            p += satisfaction[i]
            res = max(res, currSum)

            if p < 0:
                break

        return res     
