class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        
        visited = set()
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    adj_list[i + 1].append(j + 1)

        def dfs(num):       
            visited.add(num)

            for val in adj_list[num]:
                if val not in visited:
                    dfs(val)

        count = 0

        for key in adj_list:
            if key not in visited:
                count += 1
                dfs(key)

        return count