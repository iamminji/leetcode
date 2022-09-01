## 문제

doubly linked list 를 flatten 하게 만드는 문제다.
다만 일반 linked list 랑 다르게 child 가 있고, 이 child 의 우선순위가 더 높아야 한다(?) 는 것이다.

### 솔루션
child 가 먼저 선행 되어야 하기 때문에 depth 를 두고, queue 를 heap 으로 써서(child 를 queue 에서 먼저 꺼내려고) bfs 로 풀었다.

코드 참고
```python3
class Solution:
    def flatten(self, head: 'Node') -> 'Node':

        if head is None:
            return None

        heap = []

        item = (0, head)
        heappush(heap, item)

        dummy = Node(0, None, None, None)
        result = dummy

        while heap:
            depth, node = heappop(heap)

            dummy.next = node
            node.prev = dummy

            if node.child is not None:
                heappush(heap, (depth - 1, node.child))
            if node.next is not None:
                heappush(heap, (depth, node.next))

            dummy = dummy.next
            dummy.next = None
            dummy.child = None

        ret = result.next
        ret.prev = None
        return ret
```

근데 막상 풀고나니까 stack 으로 할 수 있더라. next 를 먼저 넣고 child 를 나중에 넣는 식으로 하면 LIFO 이기 때문에 child 값만 먼저 확인 가능하다(!)

### 주저리
결과 값이 doubly linked list 가 아니래서 한참 헤맸는데... 알고보니 dummy 로 준 첫번째 dummy head 가 결과 값에 포함 되었었기 때문이었다.

그리고 한번 틀렸는데 (ㅠㅠ) None 이 input 으로 들어오는 것을 확인 못했다. 제발... 검토를 확실히 하자!!
