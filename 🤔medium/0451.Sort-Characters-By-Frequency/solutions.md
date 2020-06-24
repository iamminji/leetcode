## 문제 설명
문자열의 문자 개수를 세어서, 수가 많은 문자가 앞으로 오는 (정렬) 새로운 문자열을 만드는 문제다.

## 솔루션

### 방법 1 카운팅과 정렬
파이썬의 `counter`, `sorted` 를 이용해서 쉽게 구할 수 있었다. 
전체 문자열의 문자를 세고 (counter) 문자열의 개수를 기준으로 정렬 (sorted) 를 하면 된다.

> 참고로 파이썬의 sorted 는 quick sort 가 아니고 Timsort 라는 것을 사용한다.

그런데 이렇게 하면 미디엄 문제라고 하기엔 너무 쉬웠다. (그저 갓-파이썬)

```python3
from collections import Counter
from operator import itemgetter


class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        sorted_counter = sorted(counter.items(), key=itemgetter(1), reverse=True)
        res = ""
        for k, v in sorted_counter:
            res += k * v

        return res
```

### 방법 2 max-heap
1번 방법과 비슷한데, sorted 가 아니라 heap 을 써서 구할 수 있다.

> 파이썬의 `heap` 자료구조는 기본이 min-heap 이다. 따라서 max-heap 처럼 사용하고 싶으면 -1 을 곱해주는 식으로 사용하면 된다.

```pytho3
from heapq import heappop, heappush
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        heap = []
        counter = Counter(s)
        for item in s:
            heappush(heap, (-1 * counter.get(item), item))

        res = ""
        while heap:
            item = heappop(heap)
            res += item[1]

        return res
```

## 시간 복잡도
둘 다 카운팅 & 정렬을 사용하기 때문에 시간 복잡도는 O(n*logN) 이 된다. (timsort, heap sort 둘 다 O(n * logN))
공간 복잡도는 문자열 사이즈만큼인 O(n) 이 된다.
