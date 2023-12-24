class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        colum = collections.defaultdict(set)
        grid = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue

                elif (board[r][c] in rows[r] or board[r][c] in colum[c] 
                        or board[r][c] in grid[(r // 3, c // 3)]):
                    return False

                rows[r].add(board[r][c])
                colum[c].add(board[r][c])
                grid[(r // 3, c // 3)].add(board[r][c])

        return True