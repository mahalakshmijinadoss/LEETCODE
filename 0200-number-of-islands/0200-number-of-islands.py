from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        visited = set()
        
        def bfs(r, c):
            q = deque()
            visited.add((r, c))  
            q.append([r, c])  
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    new_r = row + dr
                    new_c = col + dc
                    if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == '1' and (new_r, new_c) not in visited:
                        visited.add((new_r, new_c))  
                        q.append([new_r, new_c])  
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1' and (i, j) not in visited:
                    bfs(i, j)
                    islands += 1
        
        return islands



        