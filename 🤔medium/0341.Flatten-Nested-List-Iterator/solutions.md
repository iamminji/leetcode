## 문제 설명
nested 되어있는 리스트를 flatten 하게 만드는 문제다.

## 솔루션
주어진 NestedInteger 리스트를 다 순회해서 queue 에 `append` 하고 next 를 호출하면 `popleft()` 로 값을 뺀다. (iterator 기 때문에 리스트와 인덱스가 아닌 queue 로 append, pop 을 해 주었다.)

NestedInteger 리스트를 순회하는 것은 값이 리스트인지, NestedInteger 인지 구분해서 재귀로 NestedInteger 일 때만 값을 넣는 것으로 구현하면 된다.
