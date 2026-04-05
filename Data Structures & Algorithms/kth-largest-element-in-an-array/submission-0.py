class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []  # min heap
        for _, val in enumerate(nums):
            if len(heap) == k:
                if val > heap[0]:
                    heapq.heappushpop(heap, val)
            else:
                heapq.heappush(heap, val)
        return heap[0]