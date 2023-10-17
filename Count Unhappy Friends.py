class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        match = defaultdict(int)
        for p1, p2 in pairs:
            match[p1] = p2
            match[p2] = p1

        adjList = {}
        for i in range(len(preferences)):
            for j in range(n-1):
                if i not in adjList:
                    adjList[i] = {}
                adjList[i][preferences[i][j]] = j

        res = 0
        for i in range(len(preferences)):
            for j in range(n-1):
                x = i
                y = match[x]
                u = preferences[x][j]
                v = match[u]

                if adjList[x][u] < adjList[x][y] and adjList[u][x] < adjList[u][v]:
                    res += 1
                    break

        return res
