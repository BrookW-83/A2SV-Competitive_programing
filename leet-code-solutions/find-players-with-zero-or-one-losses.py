class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        victors = [[] for i in range(2)]

        lossCount = Counter()

        for win, loss in matches:
            if win not in lossCount:
                lossCount[win] = 0
            lossCount[loss] += 1

        for match, losses in lossCount.items():
            if losses < 2:
                victors[losses].append(match)

        return [sorted(victors[0]), sorted(victors[1])]

