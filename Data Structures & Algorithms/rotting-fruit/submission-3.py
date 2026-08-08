class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()
        fresh = 0
        time = 0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c] == 2:
                    q.append((r,c))
                if grid[r][c]==1:
                    fresh+=1
        if fresh == 0:
            return 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if(0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]==1):
                        grid[nr][nc]=2
                        fresh-=1
                        q.append((nr, nc))
            time+=1
        if fresh ==0:
            return time-1
        else:
            return -1



