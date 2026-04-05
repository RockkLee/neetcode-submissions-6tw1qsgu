from collections import defaultdict, deque
from typing import List

UNVISITED = 0
VISITING = 1
VISITED = 2


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res: deque[int] = deque()
        states = [UNVISITED] * numCourses
        prereq_dic = defaultdict(list)
        for course_id, pre_course_id in prerequisites:
            prereq_dic[pre_course_id].append(course_id)

        def dfs(node: int) -> bool:
            if states[node] == VISITED:
                return True
            if states[node] == VISITING:
                return False
            # UNVISITED
            states[node] = VISITING
            for neighbor in prereq_dic[node]:
                if not dfs(neighbor):
                    return False
            states[node] = VISITED
            res.appendleft(node)
            return True

        for course in list(prereq_dic.keys()):
            if not dfs(course):
                return []
        for course in range(numCourses):
            if states[course] == UNVISITED:
                res.appendleft(course)
        return list(res)
