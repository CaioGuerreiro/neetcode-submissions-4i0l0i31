class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_rows = len(grid)
        num_cols = len(grid[0])
        visited = set()
        res = 0

        def get_island(coord):
            r, c = coord
            delta_cols = [1, 0, -1, 0]
            delta_rows = [0, -1, 0, 1]

            for i in range(len(delta_rows)):
                neighbor_rows = r + delta_rows[i]
                neighbor_cols = c + delta_cols[i]
                if 0 <= neighbor_rows < num_rows and 0 <= neighbor_cols < num_cols:
                    if grid[neighbor_rows][neighbor_cols] == '1':
                        yield neighbor_rows, neighbor_cols



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
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs((r,c))
                    res +=1
        return res
"""
1) fazer uma função que percorrar as casas dos 4 eixos
2) fazer um bfs
3) achar uma "ilha"

"""


