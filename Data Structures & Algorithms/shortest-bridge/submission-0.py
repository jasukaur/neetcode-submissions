class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        dirs = [(0,1), (0,-1), (1,0), (-1,0)]

        def invalid(r,c):
            return r < 0 or c <0 or r>=R or c>= C

        visit = set()

        def dfs(r, c):
            if invalid(r,c) or grid[r][c] == 0 or (r,c) in visit:
                return 
            visit.add((r,c))
            for dr, dc in dirs:
                dfs(r+dr, c+dc)
        
        def bfs():
            res, q = 0, deque(visit)

            while q:
                for _ in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in dirs:
                        cr, cc = r+dr, c+dc
                        if invalid(cr,cc) or (cr,cc) in visit:
                            continue
                        if grid[cr][cc]:
                            return res
                        q.append((cr,cc))
                        visit.add((cr,cc))
                res +=1
        
        for r in range(R):
            for c in range(C):
                if grid[r][c]:
                    dfs(r,c)
                    return bfs()