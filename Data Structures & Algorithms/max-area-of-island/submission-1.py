class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]
        visited = set()

        def dfs(r, c):
            visited.add((r, c))
            a = 1
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or (nr, nc) in visited or grid[nr][nc] == 0:
                    continue
                a += dfs(nr, nc)
            return a

        area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = max(area, dfs(r, c))
        return area