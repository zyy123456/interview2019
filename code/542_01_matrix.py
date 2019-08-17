class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        dirs = [(0, -1), (-1,0), (0,1), (1,0)]
        q = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    q.append((i,j))
                else:
                    matrix[i][j] = float('inf')
        while q:
            t = q.pop(0)
            for dir in dirs:
                x = t[0] + dir[0]
                y = t[1] + dir[1]
                if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= matrix[t[0]][t[1]] + 1:
                    continue
                matrix[x][y] = matrix[t[0]][t[1]] + 1
                q.append((x,y))
        return matrix
