class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        queue = deque()
        visited =  set()
        
        def get_neighbor(r,c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == -1 or (r,c) in visited:
                return 
            queue.append([r,c])
            visited.add((r,c))


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append([r,c])
                    visited.add((r,c))
        
        dist = 0
        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                grid[r][c] = dist
                get_neighbor(r+1,c)
                get_neighbor(r-1,c)
                get_neighbor(r,c+1)
                get_neighbor(r,c-1)
            dist += 1


"""
Input: [
  [#,-1,0,#],
  [#,#,#,-1],
  [#,-1,#,-1],
  [0,-1,#,#]
]

Output: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]

"""