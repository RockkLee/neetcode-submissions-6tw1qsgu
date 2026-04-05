class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minheap = nums
        heapq.heapify(self.minheap)
        self.window = k
        while len(self.minheap) > self.window:
            heapq.heappop(self.minheap)


    def add(self, val: int) -> int:
        heapq.heappush(self.minheap, val)
        if len(self.minheap) > self.window:
            heapq.heappop(self.minheap)
        return self.minheap[0]
