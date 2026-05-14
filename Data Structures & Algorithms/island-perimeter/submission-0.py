class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def bfs(r, c):
            queue = deque([(r,c)])
            visited.add((r,c))
            perimeter = 0

            while queue:
                cr, cc = queue.popleft()

                for dr, dc in dirs:
                    nr, nc = cr+dr, cc+dc

                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] == 0:
                        perimeter += 1
                    elif (nr, nc) not in visited:
                        visited.add((nr,nc))
                        queue.append((nr,nc))
            return perimeter


        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return bfs(r,c)
        return 0