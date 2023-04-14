class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        direction = [(1,0), (-1,0), (0, 1), (0,-1)]
        visited = set()

        inBound = lambda row, col: 0 <= row < len(image) and 0 <= col < len(image[0])

        def dfs(row, col, val):

            visited.add((row, col))

            for i, j in direction:
                new_row = row + i
                new_col = col + j
                print(new_row, new_col)
                

                if inBound(new_row, new_col)  and image[new_row][new_col] == val and (new_row, new_col) not in visited:
                    image[new_row][new_col] = color
                    dfs(new_row, new_col, val)
        


        for row in range(len(image)):
            for col in range(len(image[0])):
                tmp = image[sr][sc]
                image[sr][sc] = color
                dfs(sr, sc, tmp)
                break

        return image