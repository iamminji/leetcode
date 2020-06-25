## 문제 설명
내장된 `hashSet` 라이브러리 사용 없이 `hashSet` 을 구현하는 문제다.
자바의 `hashTable` 이 어떻게 구현되었는지 알고 있었기 때문에 구조는 쉽게 잡을 수 있었다.

[참고](https://www.geeksforgeeks.org/implementing-our-own-hash-table-with-separate-chaining-in-java/)

## 솔루션
자바의 `hashTable` 은 값을 `hash` 연산하여 리스트에 넣고, `hash collision` 이 발생하면 해당 리스트의 값에서 `LinkedList` 로 chaining 하게 이어지게 된다.

문제에서 들어오는 값의 다양성(?) 종류(?) 최대 사이즈(?) 가 10000 개라고 명시했기 때문에 10000 개의 사이즈의 배열을 만들어준다.

```
The number of operations will be in the range of [1, 10000].
```

파이썬으로 이 구조로 구현했다. hash 계산을 위해 모듈러 연산을 사용해 그 값을 키 (index) 로 사용했고 index 가 겹치면 (collision) 이 일어나면 ListNode 로 chaining 하게 연결하였다.
