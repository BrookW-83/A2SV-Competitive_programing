class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        for i,j in sorted(tickets, reverse = True):
            graph[i].append(j)


        seen = []
        def dfs(curr):
            while graph[curr]:
                dfs(graph[curr].pop())
            seen.append(curr)

        dfs("JFK")

        return seen[::-1]