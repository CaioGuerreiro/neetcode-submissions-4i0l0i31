class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        visited = set()
        res = 0

        def get_island(coord):
            row, col = coord
            delta_row = [1, 0, -1, 0]
            delta_col = [0, 1, 0, -1]
            for i in range(len(delta_row)):
                neighbor_row = row + delta_row[i]
                neighbor_col = col + delta_col[i]
                if 0 <= neighbor_row < num_rows and 0 <= neighbor_col < num_cols:
                    if grid[neighbor_row][neighbor_col] == '1':
                        yield neighbor_row, neighbor_col

          


        def bfs(root):
            queue = deque([root])
            visited.add(root)

            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    for island in get_island(node):
                        if island in visited:
                            continue
                        visited.add(island)
                        queue.append(island)
        
        for r in range(num_rows):
            for c in range(num_cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs((r,c))
                    res += 1
        return res
"""
1) fazer uma função que percorrar as casas dos 4 eixos
2) fazer um bfs
3) achar uma "ilha"

"""


