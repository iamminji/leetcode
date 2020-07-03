## 문제
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.

Given n, find the total number of full staircase rows that can be formed.

n is a non-negative integer and fits within the range of a 32-bit signed integer.

```
Example 1:

n = 5

The coins can form the following rows:
¤
¤ ¤
¤ ¤

Because the 3rd row is incomplete, we return 2.
Example 2:

n = 8

The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤

Because the 4th row is incomplete, we return 3.
```

### 솔루션
n 이라는 수가 들어왔을 때 1씩 증가하는 수열 `a + (a+1) + (a+2) + ... + (a+k) <= n` 에서 만족하는 `k` 를 찾는 문제였다.
이를 수식으로 풀면 된다.

#### 해결 1
1씩 증가하는 수열의 합은 (고등학생 때 다들 배웠겠지만...) `k * (k+1) / 2` 이니까 이 값이 주어진 값 n 을 안넘게 하는 k 를 찾으면 된다.
코드에서 이 k 값은 a 이고 k * (k+1) 은 b 로 두고 while 문을 돌렸다.

```python3
class Solution:
    def arrangeCoins(self, n: int) -> int:

        a = 1
        b = 2
        while b <= (2 * n):
            a += 1
            b = (pow(a, 2) + a)

        return a - 1
```

#### 해결 2
이 코드도 돌아가지만 결국 공식은 `k * (k+1) / 2 <= 2 * n` 이므로 n 은 알고 있으니까 k를 변수로 두고 식을 풀어쓸 수도 있다.
k를 대상으로 완전 제곱식을 만들면 된다. 이 때 만족하는 k 는 정수인데, sqrt 해서 나온 결과 값은 float 이므로 int 로 캐스팅 해준다.
(캐스팅 해주는 이유는 위의 코드에서 -1 하는 것과 같음)

```python3
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int(sqrt((2 * n) + 0.25) - 0.5)
```

이 방법의 경우 수학 공식이기 때문에 해결 1 보다 훨씬 빠르다.