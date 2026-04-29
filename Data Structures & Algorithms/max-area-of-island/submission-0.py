class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        maxArea = 0
        ROWS, COLS = len(grid), len(grid[0])
        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r, c):
            if (
                r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or 
                grid[r][c] == 0 or 
                (r, c) in visited
            ):
                return 0
            
            visited.add((r, c))

            area = 1

            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc
                area += dfs(nr, nc)

            return area

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    maxArea = max(maxArea, dfs(r, c))

        return maxArea