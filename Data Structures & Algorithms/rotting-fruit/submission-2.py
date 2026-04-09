class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        time = -1
        visited = set()


        def get_neighbor(r,c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] != 1 or grid[r][c] in visited:
                return
            nonlocal fresh
            grid[r][c] = 2
            fresh -= 1
            visited.add((r,c))
            queue.append([r,c])
        
        queue = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    queue.append([r,c])
                    visited.add((r,c))
        
        if fresh == 0:
            return 0
        
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                get_neighbor(r+1,c)
                get_neighbor(r-1,c)
                get_neighbor(r,c+1)
                get_neighbor(r,c-1)
                
            time += 1
        return time if fresh == 0 else -1




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