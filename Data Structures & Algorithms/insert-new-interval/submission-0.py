import copy
from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [new_interval]
        if len(intervals) == 1:
            if new_interval[1] < intervals[0][0]:
                return [new_interval, intervals[0]]
            elif new_interval[0] > intervals[0][1]:
                return [intervals[0], new_interval]
            elif new_interval[0] < intervals[0][0] and new_interval[1] <= intervals[0][1]:
                return [[new_interval[0], intervals[0][1]]]
            elif  new_interval[0] >= intervals[0][0] and new_interval[1] > intervals[0][1]:
                return [[intervals[0][0], new_interval[1]]]
            elif new_interval[0] < intervals[0][0] and new_interval[1] > intervals[0][1]:
                return [copy.deepcopy(new_interval)]
            else:
                return copy.deepcopy(intervals)

        ls: List[List[int]] = []
        if new_interval[0] <= intervals[0][0]:  # new_interval is in the left of the first interval
            ls.append(new_interval)
            for interval in intervals: ls.append(interval)
        elif new_interval[0] >= intervals[-1][0]:  # new_interval is in the right of the last interval
            ls = copy.deepcopy(intervals)
            ls.append(new_interval)
        elif len(intervals) == 2:
            ls = [intervals[0], new_interval, intervals[1]]
        else:  # len(intervals) > 2 and new_interval is inside the "intervals"
            for idx in range(len(intervals) - 1):
                ls.append(intervals[idx])
                if intervals[idx][0] <= new_interval[0] <= intervals[idx + 1][0]:
                    ls.append(new_interval)
            ls.append(intervals[-1])

        output: List[List[int]] = [ls[0]]
        for interval in ls:
            start, end = interval[0], interval[1]
            if start > output[-1][1]:
                output.append(interval)
            elif start >= output[-1][0] and end > output[-1][1]:
                output[-1][1] = end

        return output
