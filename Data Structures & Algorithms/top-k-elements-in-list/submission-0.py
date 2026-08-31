from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        hp: List[tuple[int, int]] = []
        for num in freq.keys():
            heapq.heappush(hp, (freq[num], num))
            if len(hp) > k:
                heapq.heappop(hp)
        
        res: List[int] = []
        for f, num in hp:
            res.append(num)
        return res
