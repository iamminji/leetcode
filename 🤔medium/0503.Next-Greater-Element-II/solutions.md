## 문제 설명
배열의 각 원소의 바로 다음 번의 큰 원소 값을 현재 원소 인덱스에 해당하는 곳에 넣는 문제다.
글로 풀어쓰니 복잡한데, 문제 자체는 심플하다.

```
Input: [1,2,1]
Output: [2,-1,2]
```

- 0번째 인덱스의 값 1 보다 바로 그 다음에 큰 값은 1번째 인덱스의 값 2 이고
- 1번째 인덱스의 값 2 보다 바로 그 다음에 큰 값은 없다. 그래서 -1
- 2번째 인덱스의 값 1 보다 바로 그 다음에 큰 값은 1번째 인덱스의 값 2다.

circular 하다고 보면 된다. 그래서 2번째 인덱스가 가장 마지막 원소지만 다시 첨으로 돌아가서 순회하는 것이다.

## 솔루션
circular 하다고 볼 수 있어서 배열 * 2 만큼 순회한다고 생각했다.
코드는 아래와 같다. 통과는 하는데 굉장히 느리다.

```python3
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        cur_idx, idx = 0, 1
        size = len(nums)
        ans = [-1 for _ in range(size)]

        while cur_idx < size:
            if nums[cur_idx] < nums[idx % size]:
                ans[cur_idx] = nums[idx % size]
                cur_idx += 1
                idx = cur_idx + 1
            else:
                # 되돌아옴
                if cur_idx == (idx % size):
                    cur_idx += 1
                else:
                    idx += 1

        return ans
```

`cur_idx` 는 현재 인덱스고 `idx` 는 순회하면서 비교할 대상 인덱스다. 

현재 값 보다 크면 `ans` 를 업데이트 해 주고 `cur_idx`, `idx` 를 증가시킨다.
현재 값 보다 가르키는 (비교 대상) 이 작으면 인덱스를 계속 증가시키는데, 단 자기 자신으로 돌아올 수도 있기 때문에 (circular!) 이 경우엔 현재 인덱스를 증가시켜버린다.

그림으로 보면 아래와 같다.

```
[step1]
cur_idx     idx
1           2           1           1           2            1

ans = [2, -1, -1]

[step2]
            cur_idx     idx
1           2           1           1           2           1

ans = [2, -1, -1]

[step3]
            cur_idx                 idx
1           2           1           1           2           1

ans = [2, -1, -1]

[step4]
            cur_idx                             idx
1           2           1           1           2           1

ans = [2, -1, -1]

[step5]
                        cur_idx                 idx
1           2           1           1           2           1

ans = [2, -1, -1]

[step6]
                        cur_idx                 idx
1           2           1           1           2           1

ans = [2, -1, 2]
```


## 복잡도
시간 복잡도는 처음엔 배열의 사이즈 * 2라고 생각해서 O(2n) 즉 O(n) 이라고 생각했는데, 
결국 cur_idx, idx 가 같이 증가하면서 순회하므로 O(n^2) 이 되는 것...같다.

공간 복잡도는 ans 사이즈가 배열 사이즈와 같으므로 O(n) 이다.

릿코드 솔루션을 보니 O(n) 으로도 풀 수 있는데, 스택을 이용하면 된다고 한다.
이 방식도 풀어보도록 하자!
