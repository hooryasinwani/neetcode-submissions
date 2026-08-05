class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = collections.deque()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c]==0:
                    q.append((r,c))
        
        while q:
            r,c = q.popleft()
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if(0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc]==2147483647):
                    grid[nr][nc]= grid[r][c]+1
                    q.append((nr, nc))
        


