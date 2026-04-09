class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])

        def backtrack(r,c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or board[r][c] != 'O':
                return
            board[r][c] = '#'
            backtrack(r+1,c)
            backtrack(r-1,c)
            backtrack(r,c+1)
            backtrack(r,c-1)


        for r in range(ROWS):
            for c in range(COLS):
                if (board[r][c] == 'O' and (r == 0 or r == ROWS - 1) or (c == 0 or c == COLS -1)):
                    backtrack(r,c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == '#':
                    board[r][c] = 'O'
        
"""
Input: board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","O","O","X"],
  ["X","X","X","O"]
]


"""        
        