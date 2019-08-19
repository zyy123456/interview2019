# DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        res = 0
        row, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(row)]
        for i in range(row):
            for j in range(cols):
                if visited[i][j] or grid[i][j] == '0': continue
                self.helper(visited, grid, i, j)
                res += 1
        return res
    
    def helper(self, visited, grid, i, j):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or visited[i][j] or grid[i][j] == '0':
            return 
        visited[i][j] = True
        self.helper(visited, grid, i - 1, j)
        self.helper(visited, grid, i + 1, j)
        self.helper(visited, grid, i, j - 1)
        self.helper(visited, grid, i, j + 1)

 # BFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]: return 0
        res = 0
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        dirs = [(-1,0), (1, 0), (0, 1), (0, -1)]
        for i in range(m):
            for j in range(n):
                if visited[i][j] or grid[i][j] == '0': continue
                res += 1
                q = [(i, j)]
                while q:
                    t = q.pop(0)
                    for k in range(4):
                        x, y = t[0] + dirs[k][0], t[1] + dirs[k][1]
                        if x < 0 or x >= m or y < 0 or y >= n or grid[x][y] == '0' or visited[x][y]: continue
                        visited[x][y] = True
                        q.append((x,y))
        return res
