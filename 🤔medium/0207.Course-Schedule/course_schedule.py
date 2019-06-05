# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/

from collections import defaultdict


class Solution:
    WHITE = 0
    GRAY = 1

    def dfs(self, course, graph, color):

        # 이미 방문 함
        if color[course] == self.GRAY:
            return False

    def canFinish(self, numCourses: 'int', prerequisites: 'List[List[int]]') -> 'bool':
        graph = defaultdict(list)
        color = defaultdict(int)

        for num in range(numCourses):
            color[num] = self.WHITE

        for course in prerequisites:
            graph[course[0]].append(course[1])


if __name__ == '__main__':
    sol = Solution()
    print(sol.canFinish(2, [[1, 0]]))
    print(sol.canFinish(2, [[1, 0], [0, 1]]))
    print(sol.canFinish(3, [[1, 0], [3, 1], [3, 2]]))
