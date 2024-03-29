import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        m, n = len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                heapq.heappush(heap, -matrix[i][j])
                if len(heap) > k:
                    heapq.heappop(heap)
        return -heapq.heappop(heap)
