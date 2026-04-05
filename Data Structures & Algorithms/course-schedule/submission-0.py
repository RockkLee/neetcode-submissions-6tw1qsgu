from collections import defaultdict
from typing import List

UNVISITED = 0
VISITING = 1
VISITED = 2


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dic = defaultdict(list)
        for course_id, pre_course_id in prerequisites:
            dic[course_id].append(pre_course_id)

        state = [UNVISITED] * numCourses

        def dfs(node: int) -> bool:
            if state[node] == VISITING:  # back-edge → cycle
                return False
            if state[node] == VISITED:  # already checked, no cycle from here
                return True

            state[node] = VISITING
            for v in dic[node]:
                if not dfs(v):
                    return False
            state[node] = VISITED
            return True

        for course in range(numCourses):
            if state[course] == 0:
                if not dfs(course):
                    return False
        return True
