class Solution:
    def pacificAtlantic(self, heights):
        pac, atl = set(), set()
        
        def dfs(r, c, visited, prevHeight):
            if (r < 0 or r >= len(heights) or
                c < 0 or c >= len(heights[0]) or
                (r,c) in visited or
                heights[r][c] < prevHeight):
                return
            visited.add((r,c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])
        
        # Pacific: top row + left column
        for c in range(len(heights[0])):
            dfs(0, c, pac, heights[0][c])
        for r in range(len(heights)):
            dfs(r, 0, pac, heights[r][0])

        # Atlantic: bottom row + right column
        for c in range(len(heights[0])):
            dfs(len(heights)-1, c, atl, heights[len(heights)-1][c])
        for r in range(len(heights)):
            dfs(r, len(heights[0])-1, atl, heights[r][len(heights[0])-1])
                
     
       
        
        result = []
        for r, c in pac:
            if (r, c) in atl:
                result.append([r, c])
        return result