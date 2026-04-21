class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        visited = set()
        max_island = 0

        

        def get_island(coord):
            row, col = coord
            delta_row = [-1, 0, 1, 0]
            delta_col = [0, -1, 0, 1]
            for i in range(len(delta_row)):
                neighbors_row = row + delta_row[i]
                neighbors_col = col + delta_col[i]
                if 0 <= neighbors_row < num_rows and 0 <= neighbors_col < num_cols:
                    if grid[neighbors_row][neighbors_col] == 1:
                        yield neighbors_row, neighbors_col

        def bfs(root):
            
            queue = deque([root])
            visited.add(root)
            area = 1
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    for island in get_island(node):
                        if island in visited:
                            continue
                        
                        visited.add(island)
                        queue.append(island)
                        area += 1
            return area
            

        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    atual = bfs((r,c))
                    
                    if max_island < atual:
                        max_island = atual
                        
        return max_island
        







































