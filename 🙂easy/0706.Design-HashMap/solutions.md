## 문제 설명
HashMap 을 구현하는 문제다.

## 솔루션
Java의 HashTable 구현과 비슷하게 풀었다. 리스트를 두고 key 와 리스트 사이즈간의 hash 값을 구해서 리스트의 인덱스로 사용하였다.
인덱스가 겹칠 경우 (hash collision) 링크드리스트로 노드를 만들어서 넣어두었다.

```python3
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10
        self.buckets = [Node() for _ in range(self.size)]

    def find_node(self, key: int):
        index = key % self.size
        prev = self.buckets[index]
        current = prev.next

        while current is not None:
            if current.key == key:
                return prev
            prev = prev.next
            current = current.next

        return prev

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        prev = self.find_node(key)
        if prev.next is None:
            prev.next = Node(key, value)
        else:
            # update
            prev.next.value = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        prev = self.find_node(key)
        if prev.next is None:
            return -1
        return prev.next.value

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        prev = self.find_node(key)
        if prev.next is not None:
            prev.next = prev.next.next
```

그러면 값을 가져올 때는 key % size (hash 지만 정확히 따지면 모듈러 연산) 으로 인덱스를 구하고 이 값으로 리스트 접근 하고,
노드 key 값이 input key 랑 동일하면 리턴, 아니면 노드가 링크드리스트 이므로 계속 순회하면서 key 랑 동일한 것을 찾는다.

노드 접근을 심플하게 하기 위해 현재 노드 (current) 가 아니라 찾은 노드 바로 이전 노드 (prev) 를 리턴하게 하였다.

사실 계속 wrong answer 떠서 2시간 동안 삽질 했었는데, 알고보니 put 연산에서 업데이트가 제대로 이루어지지 않았었다.
정확히 말하자면 put 에서 키가 동일하면 값만 업데이트 되어야 하는데 업데이트가 아니라 신규 노드로 값을 계속 넣어주었던 것이다. ㅠㅠ

```python3
if prev.next is None:
    prev.next = Node(key, value)
else:
    # update 를 안하고 Node(key, value) 로 엎어치고 있었다. 테스트 케이스 찾느라고 혼났다ㅜ
    prev.next.value = value
```

## 주저리
실패 이유를 찾을 수가 없어서, wrong answer 예제를 뜯어보았는데 input 값이 너무 많고 복잡하였다.
이 값을 로컬 ide 에서 돌리게 변경하는 것은... 엄청난 노가다가 예상되는 문제.

그래서 어떻게 했냐면...
실패난 input 값으로 leetcode runcode 로 돌리고 결과 값으로 leetcode 서버가 뱉어주는 json 을 살펴봤는데 expected_answer 랑 code_answer 인가 값이 있더라.
이 값을 전체 복사해서 online 에서 text diff 해주는 거 아무 사이트나 들어가서 돌려주었다.

그랬더니 틀린 부분만 딱 체크 해서 보여주더라.

원래 leetcode 에서도 제공하는 기능인데 값이 너무 많다보니....스크롤 넘기는데 한계가 있었다ㅜ
