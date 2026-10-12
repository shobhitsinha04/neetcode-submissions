class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # if not grid:
        #     return 0
        # rows, cols = len(grid), len(grid[0])
        # directions = [[-1,0],[1,0],[0,1],[0,-1]]
        # islands = 0 
        # visit = set()

        # def bfs(r,c):
        #     q = deque()
        #     visit.add((r,c))
        #     q.append((r,c))

        #     while q:
        #         row, col = q.popleft()
        #         for dr, dc in directions:
        #             r = row + dr
        #             c = col + dc
        #             if r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in visit:
        #                 q.append((r,c))
        #                 visit.add((r,c))

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1" and (r,c) not in visit:
        #             bfs(r,c)
        #             islands += 1
        # return islands

        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        islands = 0
        directions = [[-1,0],[1,0],[0,1],[0,-1]]

        def dfs(r,c):
            if r<0 or c < 0 or r>=rows or c>= cols or grid[r][c] == "0":
                return
            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r+dr, c+dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    dfs(r,c)
                    islands += 1
        return islands