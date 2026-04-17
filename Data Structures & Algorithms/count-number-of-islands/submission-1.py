class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        islands = 0
        dirs = [(0,1), (0, -1), (-1,0), (1,0)]

        def dfs(r,c):
            visited.add((r,c))

            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc

                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS or grid[nr][nc] == "0" or (nr, nc) in visited:
                    continue
                visited.add((nr,nc))
                dfs(nr,nc)



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] =='1' and (r,c) not in visited:
                    dfs(r,c)
                    islands +=1
        return islands

