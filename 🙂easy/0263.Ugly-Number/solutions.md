## 문제 설명
input 값이 2, 3, 5 의 곱셈 조합으로 만들 수 있는 수인지 리턴하는 문제이다.

## 솔루션
input 값을 2, 3, 5 로 계속 나누어서 몫이 1이면 True 를 리턴하게 하고 아니면 False 를 리턴하게 했는데,
이 때 _아니다_ 라는 조건을 _input 값을 2, 3, 5 로 나누지 못하고 한번의 iteration 을 그대로 통과 하면_ 으로 두고 했다.

코드는 아래와 같다.

```python3
class Solution:

    def isUgly(self, num: int) -> bool:

        if num == 0:
            return False
        skip = False
        while num != 1:
            if skip:
                return False
            do = False
            if num % 2 == 0:
                do = True
                num /= 2
            if num % 3 == 0:
                do = True
                num /= 3
            if num % 5 == 0:
                do = True
                num /= 5

            if not do:
                skip = True
        return True
```

### 복잡도
공간 복잡도는 상수 값이고, 시간 복잡도는 O(n) 이 될 것 같다. (아마도?)
