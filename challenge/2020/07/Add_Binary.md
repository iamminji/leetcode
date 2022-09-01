## 문제
binary 형식의 문자열 두개가 주어지고 두 값을 binary 로 더 했을 때 나오는 binary 형태의 문자열을 리턴하는 문제다.

### 솔루션
각 문자열의 뒤에서 부터 값을 더하면서 1,1 일 경우 carry (코드에선 r) 를 1로 바꿔주었다. 그리고 각 값에 따라 배열에 넣어주었다.
결과 값은 거꾸로 인덱스를 감소 시키면서 더했기 때문에 리스트를 뒤집어서 리턴했다.

흔히 하는 덧셈 공식을 문자열로 풀이한 것이다.

```python3
class Solution:
    def addBinary(self, a: 'str', b: 'str') -> 'str':

        if len(a) == 0 and len(b) != 0:
            return b
        if len(b) == 0 and len(a) != 0:
            return a
        i, j = len(a) - 1, len(b) - 1
        r = "0"

        result = []

        while i >= 0 and j >= 0:
            p, q = a[i], b[j]
            if r == "1":
                if p == "1" and q == "1":
                    result.append("1")
                elif (p == "1" and q == "0") or (p == "0" and q == "1"):
                    result.append("0")
                else:
                    result.append("1")
                    r = "0"
            else:
                if p == "1" and q == "1":
                    result.append("0")
                    r = "1"
                elif p == "0" and q == "0":
                    result.append("0")
                else:
                    result.append("1")
            i -= 1
            j -= 1

        if len(a) > len(b):
            while i >= 0:
                if r == "1":
                    if a[i] == "1":
                        result.append("0")
                        r = "1"
                    else:
                        result.append("1")
                        r = "0"
                else:
                    result.append(a[i])
                i -= 1
        elif len(b) > len(a):
            while j >= 0:
                if r == "1":
                    if b[j] == "1":
                        result.append("0")
                        r = "1"
                    else:
                        result.append("1")
                        r = "0"
                else:
                    result.append(b[j])
                j -= 1

        if r == "1":
            result.append(r)

        return "".join(result[::-1])
```

코드를 더 깔끔하게 할 수도 있을 것 같은데, 그것은 중요하지 않으니 패스.

시간 복잡도는 문자열 길이가 큰 쪽에 영향을 받는다. 만약 각각 N, M 길이의 문자열이고 N < M 이면 O(M) 이 될 것이다.
공간 복잡도 역시 O(M) 이다.