# https://leetcode.com/problems/unique-paths/
# 62. Unique Paths


class Solution:
    def recursive(self, m, n, i, j, visited):

        if i > m - 1 or j > n - 1:
            return 0

        if (i, j) in visited:
            return visited[(i, j)]

        # 끝에 왔음
        if i == m - 1 and j == n - 1:
            return 1

        a = self.recursive(m, n, i + 1, j, visited)
        b = self.recursive(m, n, i, j + 1, visited)

        visited[(i, j)] = a + b
        return a + b

    def uniquePaths(self, m: int, n: int) -> int:
        return self.recursive(m, n, 0, 0, {})


if __name__ == '__main__':
    sol = Solution()
    ans = sol.uniquePaths(23, 12)
    print(ans)
