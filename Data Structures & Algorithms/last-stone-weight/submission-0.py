class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1
            
        heapq.heapify(stones)
        while stones:
            first = heapq.heappop(stones)
            if not stones:
                return - first
            second = heapq.heappop(stones)
            val = (- first) - (- second)
            heapq.heappush(stones, - val)
        return -1
