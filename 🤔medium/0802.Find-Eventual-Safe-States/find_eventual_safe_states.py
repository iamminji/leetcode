# 802. Find Eventual Safe States
# https://leetcode.com/problems/find-eventual-safe-states/


from collections import defaultdict


class Solution(object):
    UN_VISIT = 0
    UN_SAFE = 1
    SAFE = 2

    def is_safe(self, status, graph, node):

        # cache
        if status[node] != self.UN_VISIT:
            return status[node] == self.SAFE

        # not visit yet
        status[node] = self.UN_SAFE
        for n in graph[node]:
            # 이미 UN_SAFE(되 돌아옴) 한 경우 바로 리턴
            if status[n] == self.UN_SAFE:
                return False
            # dfs
            if not self.is_safe(status, graph, n):
                return False

        # graph[node] 를 전부 확인하였지만 되 돌아오지(un safe 하지) 않았기 때문에
        # safe 로 업데이트 해 준다.
        status[node] = self.SAFE
        return True

    def eventualSafeNodes(self, graph):
        status = defaultdict(int)
        result = []

        for node, nodes in enumerate(graph):
            # if is safe
            if self.is_safe(status, graph, node):
                result.append(node)
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.eventualSafeNodes([[1], [2, 3], [5], [0], [5], [], []]))  # [2,4,5,6]
