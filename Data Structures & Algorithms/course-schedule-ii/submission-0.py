from collections import defaultdict, deque
from typing import List, Tuple

UNVISITED = 0
VISITING = 1
VISITED = 2


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [i for i in range(numCourses)]

        # nodes
        con_node_dic: dict[int, int] = dict()
        orphans: List[int] = []
        nodes = set()

        # edges
        edge_dic = defaultdict(list)
        backward_edge_dic = defaultdict(list)
        for course, pre_course in prerequisites:
            nodes.add(course)
            nodes.add(pre_course)
            edge_dic[course].append(pre_course)
            backward_edge_dic[pre_course].append(course)

        # create connected nodes and orphans
        for c in range(numCourses):
            if c in nodes:
                con_node_dic[c] = UNVISITED
            else:
                orphans.append(c)

        def dfs(c: int, path: List[int]) -> bool:
            con_node_dic[c] = VISITING
            for neighbor in edge_dic[c]:
                if con_node_dic[neighbor] == VISITING:
                    return False
                if con_node_dic[neighbor] == VISITED:
                    continue
                if not dfs(neighbor, path):
                    return False
            if con_node_dic[c] == VISITING:
                con_node_dic[c] = VISITED
                path.append(c)
            return True

        res = []
        for c in con_node_dic.keys():
            if c in backward_edge_dic:
                continue
            # dfs
            if not dfs(c, res):
                return []

        # check if all connected nodes are visited
        for node, status in con_node_dic.items():
            if status != 2:
                return []
        return res + orphans
