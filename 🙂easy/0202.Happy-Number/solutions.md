## 문제 설명
주어진 숫자를 쪼개서 각각 제곱을 하고 더한 값이 1이 되면 True, 아니면 False 를 리턴하는 문제다.

## 솔루션
제곱을 하고 더한 값을 계속 반복하는데, 만약 이미 계산했던 수 조합이 또 등장한다면 결국 1이 될 수는 없다는 것이다.
했던 수가 또 나오면 바로 반복문을 종료하면 된다.

```python3
class Solution:
    def isHappy(self, n: int) -> bool:

        skip = set()
        while n > 1:
            res = 0
            for c in str(n):
                res += pow(int(c), 2)
            if res in skip:
                break
            skip.add(res)
            n = res

        return n == 1
```

> 찾아보니까 Cycle detection 으로 구하는 경우도 있더라. 반복해서 등장하는 수를 나는 skip 이라는 set 을 이용하였는데, Floyd algorithm 을 써서 찾더라. 정말 세상엔 천재들이 많다..
