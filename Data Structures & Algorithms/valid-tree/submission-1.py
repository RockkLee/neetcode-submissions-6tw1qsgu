from collections import defaultdict
from typing import List

UNVISITED = -1
VISITING = 0
VISITED = 1

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        states = [UNVISITED] * n
        dic: dict[int, List[int]] = defaultdict(list)
        for edge in edges:
            n1, n2 = edge[0], edge[1]
            dic[n1].append(n2)
            dic[n2].append(n1)

        def dfs(node: int, prenode: int) -> bool:
            if states[node] == VISITED:
                return True
            if states[node] == VISITING:
                return False
            # UNVISITED
            states[node] = VISITING
            for neighbor in dic[node]:
                if prenode == neighbor:
                    continue
                if states[neighbor] == VISITING:
                    return False
                if states[neighbor] == UNVISITED:
                    dfs(neighbor, node)
            states[node] = VISITED
            return True

        if not dfs(0, -1):
            return False
        for node in range(n):
            if states[node] != VISITED:
                return False
        return True
