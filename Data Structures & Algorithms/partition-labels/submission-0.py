from collections import defaultdict
from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        dic: [str, List[str]] = defaultdict(list)
        for i, c in enumerate(s):
            if len(dic[c]) < 2:
                dic[c].append(i)
                continue
            dic[c][1] = i
        intervals = sorted(dic.values(), key=lambda v: v[0])
        for interval in intervals:
            if len(interval) == 1: interval.append(interval[0])

        ls = [intervals[0]]
        for interval in intervals:
            start = interval[0]
            end = interval[1]
            if start > ls[-1][1]:
                ls.append([start, end])
                continue
            if start >= ls[-1][0] and end > ls[-1][1]:
                ls[-1][1] = end
                continue
        return list(map(lambda _interval: _interval[1] - _interval[0] + 1, ls))
