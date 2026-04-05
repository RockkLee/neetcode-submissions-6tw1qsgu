from collections import Counter, deque
import heapq
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count tasks and build a max-heap of remaining counts (as negatives)
        freq = Counter(tasks)
        heap = [-cnt for cnt in freq.values()]
        heapq.heapify(heap)

        # cooldown holds (ready_time, neg_count) and is kept in increasing ready_time
        cooldown = deque()  # ele: (time, -cnt)

        time = 0
        while heap or cooldown:
            # 1) Release any tasks whose cooldown expired by current time
            while cooldown and cooldown[0][0] <= time:
                _, negcnt = cooldown.popleft()
                heapq.heappush(heap, negcnt)

            # 2) If we have a task available, run one instance
            if heap:
                negcnt = heapq.heappop(heap)  # most frequent remaining
                negcnt += 1                   # we used one: -k -> -(k-1) so we add 1 toward zero
                if negcnt != 0:               # still have remaining copies of this task
                    # Next time this same task can run is time + n + 1
                    cooldown.append((time + n + 1, negcnt))

            # 3) One unit of time passes (idle or busy)
            time += 1

        return time
