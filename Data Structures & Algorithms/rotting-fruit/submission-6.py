class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # if not grid or not grid[0]:
        #     return 0
        # rows = len(grid)
        # cols = len(grid[0])
        # # to hold rotten oranges
        # q = deque()
        # fresh = 0

        # # find fresh and rotten oranges
        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == 1:
        #             fresh += 1
        #         elif grid[r][c] == 2:
        #             q.append((r,c,0))
        
        # if fresh == 0:
        #     return 0
        # dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        # minutes = 0
        # while q:
        #     r,c,t = q.popleft()
        #     minutes = max(minutes, t)
        #     for dr, dc in dirs:
        #         nr = r + dr
        #         nc = c + dc
        #         if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
        #             continue
        #         if grid[nr][nc] != 1:
        #             continue
        #         grid[nr][nc] = 2
        #         fresh -= 1
        #         q.append((nr, nc, t+1))
        # if fresh != 0:
        #     return -1
        # return minutes
        rows = len(grid)
        cols = len(grid[0])
        queue = deque()
        fresh = 0 
        minutes = 0
        # count fresh fruits get all rotten fruits in queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    fresh += 1
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        # processing minute at a time
        while queue and fresh > 0:
            for _ in range(len(queue)):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    # check bounds and whether fresh fruit
                    if ( 0<= nr < rows) and (0 <= nc < cols) and (grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))
            minutes += 1
        return minutes if fresh == 0 else -1


        