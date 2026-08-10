class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap = [(grid[0][0], 0, 0)]
        visited = set()
        n = len(grid)

        while heap:
            cost, r, c = heapq.heappop(heap)
            if (r,c) in visited:
                continue
            visited.add((r, c))
            if r == n-1 and c == n-1:
                return cost
            for nr, nc in [(r+1,c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0<=nr<n and 0<=nc<n and (nr, nc) not in visited:
                    heapq.heappush(heap, (max(cost, grid[nr][nc]), nr, nc ))