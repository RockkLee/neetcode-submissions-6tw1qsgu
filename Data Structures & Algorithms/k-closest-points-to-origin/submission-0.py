class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []  # min heap
        for _, point in enumerate(points):
            distance = point[0] ** 2 + point[1] ** 2
            if len(heap) == k:
                heapq.heappushpop(heap, (-distance, point))
            else:
                heapq.heappush(heap, (-distance, point))
        return [point for (dist, point) in heap]