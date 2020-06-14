## 문제 설명
주어진 matrix 에서 정사각형 (1로 이루어진) 을 찾는 문제다.

## 솔루션
DP 로 풀 수 있다.
2x2의 정사각형이 되려면 1x1 로 이루어진 정사각형 4개가 필요하다. 마찬가지로 3x3 정사각형이 되려면 2x2 정사각형이 포함되어 있어야 한다.
즉 정사각형의 사이즈는 이전 정사각형에 의존적이다. (그래서 DP 다.)

계산식은 다음과 같다.
```
dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + matrix[i][j]
```

1x1 정사각형 조건은 현재 지점 (i, j) 가 1이기만 하면 된다. 
그렇다면 2x2 가 되는 조건은 현재 지점을 (i, j) 라고 했을 때 (i-1, j), (j-1, i), (i-1, j-1) 들이 모두 1이기만 하면 된다.
하나라도 값이 0 이라면 이 친구는 2x2 정사각형이 될 수 없다.

이런식으로 생각해보면 현재 지점에서 정사각형 크기는 이전에 만들어진 정사각형 크기에 의존적이면서, 위, 옆, 대각선이 하나라도 0 이면 
정사각형이 될 수 없다고 볼 수 있다. (matrix[i][j] 는 0 아니면 1이기 때문에 matrix[i][j] 값을 그대로 넣어주는 거나 다름 없다. 
matrix[i][j] 가 1이면 그 친구는 1x1 의 정사각형 밖에 될 수 없다.)

## 풀이 설명
```python3
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        # dp 2차원 배열 초기화
        dp = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

        # 0번째 row, 0번째 col 을 주어진 matrix 값으로 초기화
        # 0번째 row, col 은 정사각형이 될 수 있는 경우의 수가 사이즈 1x1 정사각형 개수와 동일하다.
        # 이렇게 한 이유는 2중 for-loop 를 돌 때 배열 범위를 넘기지 않게 하기 위해서이다. (밑에서 다시 설명)
        dp[0] = matrix[0]
        for i in range(0, len(matrix)):
            dp[i][0] = matrix[i][0]

        # 1,1 부터 시작한다. 위에서 0 번째 row, 0 번째 col 계산을 했기 떄문에 1,1 부터 시작해도 된다.
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    continue
                # 여기서 배열 index 범위를 넘기는 예외 처리를 하지 않기 위해서 위에서 0 을 계산해 주고
                # 1,1 부터 for-loop 를 돈 것이다.
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + matrix[i][j]

        result = 0
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                result += dp[i][j]
        return result
```

## 참고
- https://leetcode.com/problems/count-square-submatrices-with-all-ones/discuss/643429/Python-DP-Solution-%2B-Thinking-Process-Diagrams-(O(mn)-runtime-O(1)-space)
