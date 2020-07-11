## 문제
배열에서 가장 긴 arithmetic sequence 를 찾는 문제다.
arithmetic sequence 란 배열 A[i], A[i+1], A[i+2] ... 가 있을 때 각 원소의 값의 차이가 똑같은 시퀀스 예를 들면

- `[3, 6, 9, 12, 13]` 이란 배열이 있을 때 `[3, 6, 9, 12]` 는 +3 의 차이로 이루어진 가장 긴 배열이 된다.
- `[9, 4, 7, 2, 10]` 일 경우엔 [`4, 7, 10]`이 +3 으로 가장 길게 가질 수 있는 배열이 된다.

## 솔루션
원소들의 차이를 이용한 dp 로 풀 수 있다. 

그림은 아래를 참고하면 좋을 것 같다.
[참고](https://medium.com/algorithm-and-datastructure/longest-arithmetic-sequence-567cc4eea949)

`[9, 4, 7, 2, 10]` 의 경우 가장 긴 배열은 `[4, 7, 10]` 이다. 
이를 나눠서 생각해보면 배열의 값은 `[4, 7]` 과 `[7, 10]` 의 조합이다. 즉 어떤 arithmetic sequence 를 이루려면 
임의의 배열 A[i,j] 와 배열 A[j,k] 의 조합들로 이루어져야 한다는 것이다. 그리고 이 각각의 배열에서 A[j] - A[i]와 A[k] - A[j]는 같아야 한다.


dp[(i, diff)] 는 i 번째 인덱스와 i 번째 인덱스에서 i+1 ~ k 인덱스와의 비교값 diff 의 count 를 의미한다.

예로 보면 dp[(1, 3)] 은 A[1] 인 4에서 +3 이 나온 횟수이다. (그리고 그 값은 A[2] 인 7에서 count 되었을 것이다.)
그리고 다음 루프에서 dp[(2, 3)] 이란 값이 나올 텐데, 여기서 마찬가지로 A[2] 와 A[4] 의 차이 +3 이 나온 count 다.

> 코드에서는 4-7 을 해서 사실은 -3 이란 값이 들어가지만 설명에선 헷갈리므로 +3 이라고 한다. 어차피 abs 하지 않는 이상 diff 는 상관 없다.

이걸 코드로 보면 아래와 같다

```python3
dp[(j, diff)] = dp[(i, diff)] + 1
```

i 번째에서 발생한 diff 카운팅 한 값에 1을 더하면 j 번째 발생한 diff 카운팅이 된다는 것이다. diff 는 같아야 하고 (arithmetic sequence!) 
부분 배열의 조합을 생각해야 하기 때문이다. (예를 들면 `[4, 7, 11, 14]` 에서 4와 7은 +3, 11과 14는 +3 이지만 4개를 같이 봤을 때 +3 으로 이루어진 시퀀스는 아니다!)


예제에서 나왔던 `[9, 4, 7, 2, 10]` 의 결과 배열 `[4, 7, 10]` 의 길이 값은 

1. dp[(2, 3)] 카운팅 (코드에선 2를 넣어줌)
2. dp[(4, 3)] = dp[(2, 3)] + 1

처럼 된다. 


### 코드
```python3
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = defaultdict(int)
        result = 0

        for i in range(len(A) - 1):
            for j in range(i + 1, len(A)):
                diff = A[i] - A[j]
                if (i, diff) in dp:
                    dp[(j, diff)] = dp[(i, diff)] + 1
                else:
                    dp[(j, diff)] = 2
                result = max(result, dp[(j, diff)])

        return result
```

i 번째에서 diff 란 값이 없을 때 2를 넣어준 이유는 배열이 [4, 10] 만 있다고 보면 +5 로 결과 값이 2가 되기 때문이다.
즉 배열의 사이즈가 0 또는 1이 아닌 이상 무조건 최소 값은 2가 된다.