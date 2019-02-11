# 733. Flood Fill
# https://leetcode.com/problems/flood-fill/


class Solution:

    def dfs(self, image, sr, sc, startColor, newColor, visited):
        if sc >= len(image[0]) or sr >= len(image) or sc < 0 or sr < 0:
            pass
        else:
            if image[sr][sc] == startColor and not visited[sr][sc]:
                image[sr][sc] = newColor
                visited[sr][sc] = True
                self.dfs(image, sr + 1, sc, startColor, newColor, visited)
                self.dfs(image, sr, sc + 1, startColor, newColor, visited)
                self.dfs(image, sr - 1, sc, startColor, newColor, visited)
                self.dfs(image, sr, sc - 1, startColor, newColor, visited)
        return image

    def bfs(self, image, sr, sc, startColor, newColor, visited):
        from collections import deque
        queue = deque()
        queue.append((sr, sc))

        while len(queue) > 0:
            r, c = queue.popleft()
            if c >= len(image[0]) or r >= len(image) or c < 0 or r < 0:
                continue
            if visited[r][c]:
                continue
            if image[r][c] == startColor:
                visited[r][c] = True
                image[r][c] = newColor
                queue.append((r + 1, c))
                queue.append((r, c + 1))
                queue.append((r - 1, c))
                queue.append((r, c - 1))
        return image

    def floodFill(self, image: 'List[List[int]]', sr: 'int', sc: 'int', newColor: 'int') -> 'List[List[int]]':

        visited = [[False for _ in range(len(image[0]))] for _ in range(len(image))]
        d = self.dfs(image, sr, sc, image[sr][sc], newColor, visited)
        # b = self.bfs(image, sr, sc, image[sr][sc], newColor, visited)
        return d


if __name__ == "__main__":
    sol = Solution()
    res = sol.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2)
    print(res)
