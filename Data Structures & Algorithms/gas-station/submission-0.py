class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        total, start_point = 0, 0

        for idx in range(len(gas)):
            total += (gas[idx] - cost[idx])
            if total < 0:
                total = 0
                start_point = idx + 1
        return start_point