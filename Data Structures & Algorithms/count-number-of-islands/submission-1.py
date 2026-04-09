class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        visited = set()
        res = 0

        def get_island(coord):
            row,col = coord
            delta_row = [1, 0, -1, 0]
            delta_col = [0, 1, 0, -1]
            for r in range(len(delta_row)):
                neighbors_row = row + delta_row[r]
                neighbors_col = col + delta_col[r]
                if 0 <= neighbors_row < num_rows and 0<=neighbors_col < num_cols:
                    if grid[neighbors_row][neighbors_col] == "1":
                        yield neighbors_row, neighbors_col
        
        def bfs(root):
            queue = deque([root])
            visited.add(root)
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    for island in get_island(node):
                        if island in visited:
                            continue
                        queue.append(island)
                        visited.add(island)

        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs((r,c))
                    res +=1
        
        print(visited)

        return res
    
       





