## 문제
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, calculate the Hamming distance.

Note:
```
0 ≤ x, y < 2^31.
```

Example:
```
Input: x = 1, y = 4

Output: 2

Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
```

The above arrows point to positions where the corresponding bits are different.

### 솔루션

#### 해결 1
integer 를 bin 메서드로 변경 후 최대 입력 값이 2^31 이므로 31개의 string 으로 만들어주었다.
그리고 값 비교를 누적하여 리턴하였다.

코드는 아래와 같다.

```python3
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        p = bin(x)
        q = bin(y)

        res = 0
        for a, b in zip(("%031d" % int(p[2:])), ("%031d" % int(q[2:]))):
            if a != b:
                res += 1
        return res

```

#### 해결 2
bit 값이 서로 다른 경우의 count 이므로 서로 다를 경우 1 로 해주는 exclusive or (xor) 연산을 해준다.
그리고 1 카운트를 해주었다.

```python3
    def hammingDistanceUseXor(self, x: int, y: int) -> int:
        p = x ^ y
        res = 0
        for q in bin(p)[2:]:
            if q == "1":
                res += 1
        return res
```