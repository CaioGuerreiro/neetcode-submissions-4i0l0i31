class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        fresh = 0

        def get_neighbors(r,c):
            nonlocal fresh
            if r < 0 or r == ROWS or c < 0 or c == COLS or (r, c) in visited:
                return
            elif grid[r][c] == 1:
                grid[r][c] = 2
                queue.append([r, c])
                visited.add((r, c))
                fresh -=1
            


        queue = deque()
        

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append([r, c])
                    visited.add((r, c))
                if grid[r][c]  == 1:
                    fresh +=1

        
        if fresh == 0:
            return 0
        tempo = -1
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = 2
                visited.add((r, c))
                get_neighbors(r+1, c)
                get_neighbors(r-1, c)
                get_neighbors(r, c+1)
                get_neighbors(r, c-1)
            tempo +=1
        return tempo if fresh == 0 else -1
                
"""
Input: grid = 
[
[1,1,0]
[0,1,1]
[0,1,2]
]

[1,0,1]
[0,2,0]
[1,0,1]




"""        