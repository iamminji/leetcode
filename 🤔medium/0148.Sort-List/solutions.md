## 문제 설명
링크드 리스트가 주어지는데, 상수의 공간 복잡도와 O(nlogn) 의 시간 복잡도로 정렬하는 문제다.

## 솔루션

### 꼼수
가장 쉬운 방법은 링크드 리스트를 배열로 만들어서 언어에 built-in 된 sort 함수를 사용하는 것이다.

> 참고로 python 은 timsort 라는 알고리즘으로 sort 가 구현되어 있다.

아니면 sort 함수 말고 직접 정렬을 구현하면 될 것 같다.

하지만 이러면 `constant space complexity` 를 만족할 수가 없다.

### 두뇌 풀가동
merge sort 로 하면 될 것 같았다. 이때 절반을 divide 해야 하는데 배열이랑 다르게 사이즈를 알 수가 없다. 이를 위해 fast-slow 로 노드를 순회한다.
이는 tortoise-hare 랑 비슷한데, fast 노드는 두칸씩 가고 slow 노드는 한칸씩 간다. fast 가 끝에 다다르면 slow 는 전체 링크드 리스트의 중간 노드를 가리키고 있을 것이다. 

그럼 `head ~ slow`, `slow ~ 어떤 노드` 로 나누면 된다, 이를 각각 명칭을 알기 쉽게 변경하자면 `start ~ middle`, `middle ~ end` 이다.

다만 배열과 다르게 링크드 리스트는 `middle` 노드의 다음 번째 리스트가 쭉 이어져있기 때문에 그냥 돌리면 같은 것들을 계속 확인하게 된다.
말이 조금 어려워서 다시 정리하자면 아래와 같다.

```
3 -> 1 -> 2 -> 4
```

위와 같은 링크드 리스트에서 divide 가 이루어지면 `3 -> 1`, `2 -> 4` 로 딱 나누어 떨어져야 하는데, 실제로 첫번쨰 리스트는 `3 -> 1 -> (2 -> 4)` 이렇게 되어 있다는 것이다.
이미 `2 -> 4` 는 나누어져서 다른 곳에서 어쩌고 저쩌고 할텐데, 이러면 cycle 이 되서 값이 제대로 나오지 않는다.

이를 위해 `start -> middle` 에서 `middle` 의 다음 리스트를 잘라주는 작업을 한다. 이렇게 모든 리스트를 잘라주었다면, 다음은 `merge` 작업을 진행해준다.

`merge` 작업은 두개의 노드의 값을 비교하는데, 각각을 `left`, `right` 라고 한다면 `right` 가 `left` 보다 작으면 두개를 서로 바꿔준다. 서로 바꿔주는 작업도 역시 글은 어려우니 그림으로 보자. 
아래와 같이 링크드 리스트가 있다고 할 때, 현재 `left` 와 `right` 가 아래와 같다고 해보자

```
left
1 -> 3

right
2 -> 5
```

(노드 개수가 2인 이유는 이미 divide 가 되었기 때문이고, merge 의 첫 과정이라고 생각하기 위해서이다.)

`left` 의 값이 1이고 `right` 의 값이 2 이다. 이는 정렬 되어 있으므로 `left` 를 `next` 로 이동해주자

```
left
3

right
2 -> 5
```

여기서는 정렬 되어 있지 않는다. 이럴 경우 `right` 의 `next` 와 비교한다.

```
left
3

right
5
```

`left` 보다 `right` 가 크니까 이대로 `merge` 한다. 그러면 `3 -> 5` 가 된다. 이제 거꾸로 가면 된다. 값이 작은 쪽으로 `next` 하여 비교 하였기 때문에
순서대로 `right.next` 와 `left.next` 로 올라가면서 붙여주면 된다. 정리하면 이렇게 될 것이다.

```
(1)
left
1 -> 3
right
2 -> 5

(2)
left.next 로 이동

left
3
right
2 -> 5

(3)
right.next 로 이동

left
3
right
5

(4)
merge
3 -> 5

(5)
2 -> 3 -> 5 (right: 2, back, right.next 로 붙여준다.)
(6)
1 -> 2 -> 3 -> 5 (left: 1, back, left.next 로 붙여준다.)
```

전체 코드로 보면 아래와 같다.

```python3
class Solution:

    def sortList(self, head: ListNode) -> ListNode:

        if head is None or head.next is None:
            return head

        middle = head
        fast = head.next
        slow = head.next

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            middle = middle.next

        middle.next = None

        node1 = self.sortList(head)
        node2 = self.sortList(slow)

        return self.merge(node1, node2)

    def merge(self, left, right):

        print(left, right)

        if left is None:
            return right

        if right is None:
            return left

        if left.val < right.val:
            left.next = self.merge(left.next, right)
            return left
        else:
            right.next = self.merge(left, right.next)
            return right
```

## 복잡도
시간 복잡도는 merge sort 이기에 O(nlogn) 이고 공간 복잡도는 상수 값이다.
