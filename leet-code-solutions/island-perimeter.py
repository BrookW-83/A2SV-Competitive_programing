class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        primeter = 0
        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]

        def isValid(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))

        def dfs(row, col):
            nonlocal primeter
            visited[row][col] = True

            for i, j in directions:
                new_row = row + i
                new_col = col + j

                if not isValid(new_row, new_col) or grid[new_row][new_col] == 0:
                    primeter += 1
                elif isValid(new_row, new_col) and not visited[new_row][new_col]:
                    dfs(new_row, new_col)

            return primeter

        oneFound = False
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    dfs(row, col)
                    oneFound = True
                    break

            if oneFound:
                break

        return primeter



            