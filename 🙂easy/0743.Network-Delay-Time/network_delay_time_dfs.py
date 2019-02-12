# 743. Network Delay Time
# https://leetcode.com/problems/network-delay-time/

from collections import defaultdict


class Solution:

    def dfs(self, node, g, d, r):

        # 이미 노드에 방문 했는데 기존보다 더 많은 시간이 걸린다면 계산할 필요가 없음
        if d >= r[node]:
            return

        # 시간 업데이트
        r[node] = d

        for i in sorted(g[node]):
            self.dfs(i[1], g, i[0] + d, r)

    def networkDelayTime(self, times, N, K):
        g = defaultdict(list)
        for t in times:
            g[t[0]].append((t[2], t[1]))

        r = {}
        for n in range(1, N + 1):
            r[n] = float("inf")

        self.dfs(K, g, 0, r)
        ans = r.values()
        if float("inf") in ans:
            return -1
        return max(ans)


if __name__ == '__main__':
    sol = Solution()
    print(sol.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
    print(sol.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 3))
    print(sol.networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1], [4, 1, 3]], 4, 2))
    print(sol.networkDelayTime([[1, 2, 1], [2, 1, 3]], 2, 2))
    print(sol.networkDelayTime([[1, 2, 1]], 2, 2))
    print(sol.networkDelayTime([[1, 2, 1], [2, 1, 3]], 2, 2))
    print(sol.networkDelayTime(
        [[1, 5, 66], [3, 5, 55], [4, 3, 29], [1, 2, 9], [3, 4, 10], [3, 1, 3], [2, 3, 78], [1, 4, 98], [4, 5, 21],
         [5, 2, 19], [5, 1, 76], [4, 1, 65], [3, 2, 27], [5, 3, 23], [5, 4, 12], [2, 1, 36], [4, 2, 75], [2, 4, 11],
         [1, 3, 30], [2, 5, 8]], 5, 1))
    print(sol.networkDelayTime([[1, 2, 1], [2, 3, 2], [1, 3, 2]], 3, 1))
