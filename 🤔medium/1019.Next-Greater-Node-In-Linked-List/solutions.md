## 문제 설명

## 솔루션

### 방법 1 (TLE)

2중 for 문으로 풀어봤다. 역시나 TLE 가 뜬다.
주어진 수가 내림차순일 때, 최악의 시간 복잡도 O(n^2) 을 갖게 되기 때문이다.

리스트 최대 길이가 10000 이기 때문에, 예상했던 결과였다.
```python3
class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        
        nums = []
        while head is not None:
            nums.append(head.val)
            head = head.next
        
        ans = [0 for _ in range(len(nums))]
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                if nums[i] < nums[j]:
                    ans[i] = nums[j]
                    break
        
        return ans
```

### 방법 2
스택을 이용하여 구할 수 있다.
우선 주어진 리스트 노드를 배열로 바꾼다. 

> 릿코드 디스커션을 보니 리스트 노드를 그대로 사용하는 경우도 있는데, 내 풀이 같은 경우엔 정답 리스트의 사이즈를 사전에 정의하고, 
값을 할당했기 때문에 배열로 바꾸었다.

배열 목록을 [1, 7, 5, 1, 2, 9] 라고 하자.


#### step1
초기에 스택은 비어있다.
시작 index 는 0 이다.

nums = [1, 7, 5, 1, 2, 9]
stack = []

stack 에 값을 push 한다.

#### step2
index = 1, value = 7 (nums[1] 이기 때문에)
nums = [1, 7, 5, 1, 2, 9]
stack = [(0, 1)]

stack 의 가장 첫번째 값 (자바로 따지면 peek) 과 nums[index] 를 비교한다.
stack 의 값이 nums[index] 보다 작다. 그렇다면 stack 에 들어있는 값의 next greater element 는 nums[index] 다.

stack 에는 인덱스(위의 index 와는 다르고 포인터라고 생각) 도 같이 넣었기 때문에 아래 처럼 할 수 있음

cur_index, value = stack.pop()
ans[cur_index] = nums[index]

의미는 cur_index 에 해당하는 값의 next greater element 가 nums[index] 라는 것

현재
ans = [7, 0, 0, 0, 0]

##### step3
index = 1, value = 7 (nums[1] 이기 때문에)
index = 2, value = 5
nums = [1, 7, 5, 1, 2, 9]
stack = [(1, 7)]

stack 값이 nums[index] 보다 커서 nums[index] 는 그냥 stack 에 넣어준다.

stack = [(1, 7), (2, 5)]
ans = [7, 0, 0, 0, 0]

##### step4
index = 1, value = 7 (nums[1] 이기 때문에)
step2 와 같다.
index = 3, value = 1
nums = [1, 7, 5, 1, 2, 9]
stack = [(1, 7), (2, 5), (3, 1)]
ans = [7, 0, 0, 0, 0]

##### step5
index = 4, value = 2
nums = [1, 7, 5, 1, 2, 9]
stack = [(1, 7), (2, 5), (3, 1)] -> stack = [(1, 7), (2, 5), (4, 2)]
ans = [7, 0, 0, 2, 0]

1보다 2가 크기 때문에 pop 한 후 ans 에 업데이트 한다.
업데이트 할 때는 3 번째 인덱스라는 값이 pop 할 때 나와서 ans[3] = 2 로 할 수 있는 것이다.
다만 2라는 값은 5 보다는 작기 때문에 (stack.peek) 더 이상 stack 에서 값이 빠지진 않게 된다.

##### step6 ~ 결과
index = 5, value = 9
nums = [1, 7, 5, 1, 2, 9]

stack = [(1, 7), (2, 5), (4, 2)]
ans = [7, 0, 0, 2, 9]

stack = [(1, 7), (2, 5)]
ans = [7, 0, 9, 2, 9]

stack = [(1, 7)]
ans = [7, 9, 9, 2, 9]

stack = []
index 도 nums 사이즈를 넘겨서 종료됨


9라는 값은 stack 의 peek 보다 크다. 그래서 계속 stack 에서 pop 을 해 주면서 ans 를 채워 나가게 된다.

#### 복잡도
시간 복잡도는 O(2*n) 으로 O(n) 이다. 배열의 길이만큼 순회해야 하고, 거기에 스택의 길이만큼도 순회하는데 
아무리 길어도 배열 사이즈 * 2를 넘지 않는다. (애초에 스택에 넣는 값은 배열의 값을 한번씩만 넣고, peek 을 하지 pop 해서 push 하지 않기 때문)

> 최악의 경우는 [1, 1, 1, 1, 1, 1, 1, 9] 처럼 마지막 9 를 모든 스택과 비교하게 되는 이런 경운데, 이 경우에도 n^2 이 아니고 2*n 이다.

공간 복잡도는 O(n) 이다.

