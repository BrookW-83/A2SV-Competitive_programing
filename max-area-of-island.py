class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        inBound = lambda row, col: 0 <= row < len(grid) and 0 <= col < len(grid[0])

        visited = set()

        def dfs(row, col):
            count = 1
            visited.add((row, col))

            for i, j in directions:
                new_row = row + i
                new_col = col + j

                if inBound(new_row, new_col) and grid[new_row][new_col] == 1 and (new_row, new_col) not in visited:
                    count += dfs(new_row, new_col)

            return count
  
        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in visited:
                    count = dfs(row, col)
                    max_area = max(max_area, count)


        return max_area