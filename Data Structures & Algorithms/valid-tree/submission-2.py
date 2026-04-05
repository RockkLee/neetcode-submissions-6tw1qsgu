class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        :param edges:  a list of undirected edges
        """
        dic: dict[int, List[int]] = defaultdict(list)
        for pre, cur in edges:
            dic[pre].append(cur)
            dic[cur].append(pre)

        dq = deque()
        dq.append((-1, 0))
        seen = {0}
        while dq:
            pre, cur = dq.pop()
            for nei in dic[cur]:
                if pre == nei:  # a same edge, but in diff direction
                    continue
                if nei in seen:
                    return False
                dq.append((cur, nei))
                seen.add(nei)
        return len(seen) == n
