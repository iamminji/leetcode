## 문제

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example:
```
Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16
```

### 솔루션
1과 0의 경계선의 카운트를 구하는 문제다. for loop로 1인 경우에만 확장 시켜서, 위/아래/좌/우 가 0이 나오거나 배열을 벗어나면 1로 카운트 하게 한다.
단, 그냥 하면 중복된 섬(문제에선 1이 섬이다.) 을 볼 수 있기 때문에 캐시를 두고, 이미 확인한 섬은 패스 한다.

코드는 아래와 같다.

```python3
class Solution:

    def dfs(self, i, j, grid, cache):

        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]):
            return 1

        if grid[i][j] == 0:
            return 1

        if (i, j) in cache:
            return 0

        cache[(i, j)] = True

        ans = 0
        ans += self.dfs(i, j - 1, grid, cache)
        ans += self.dfs(i, j + 1, grid, cache)
        ans += self.dfs(i + 1, j, grid, cache)
        ans += self.dfs(i - 1, j, grid, cache)

        return ans

    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        cache = dict()
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    ans += self.dfs(i, j, grid, cache)

        return ans
```

### 복잡도
공간 복잡도는 상수고, 시간 복잡도는 O(n) 이다. 
O(n) 인 이유는 캐시를 두어서 중복된 섬에서 확장 될 일이 없고, 최초에 for loop 만 있기 때문이다. (n 은 배열 길이 m*m)
