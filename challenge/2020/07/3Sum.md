## 문제
숫자 배열이 주어지고, 이 중 값 3개를 골라 0 을 만들 수 있는 모든 리스트의 조합을 리턴하는 문제다.

### 솔루션
#### stack 이용
예제에서 `[-1, 0, 1, 2, -1, -4]` 이 값에서 `-1 -> 0, -1 -> 1 ...` 이런 식으로 stack 에 넣고 빼고, backtracking 으로 구현하였다.

하지만 시간 초과 (TLE) 에 걸려서 폐기... 최대한 줄여볼려고 했는데도 잘 안되었음ㅠㅠ

여기서 더 어떻게 줄일 수 있을까?
일단은, 알고리즘 자체가 틀린 것 같았다. 따흐흑...

```python3
from copy import deepcopy
from collections import defaultdict


class Solution:

    def dfs(self, nums, index, stack, result, cache):

        if index > len(nums) or len(stack) > 3:
            return

        s = sorted(stack)
        if len(stack) == 3:
            if (s[0], s[1]) in cache:
                return
            if (s[0], s[2]) in cache:
                return
            if (s[1], s[2]) in cache:
                return
            if sum(stack) == 0:
                cache[(s[0], s[1])] = True
                cache[(s[1], s[2])] = True
                cache[(s[0], s[2])] = True
                result.append(deepcopy(stack))
            return
        

        if len(stack) == 2:
            if (s[0], s[1]) in cache:
                return
            
        for j in range(index, len(nums)):
            stack.append(nums[j])
            self.dfs(nums, j + 1, stack, result, cache)
            stack.pop()

        if len(stack) == 2:
            cache[(s[0], s[1])] = True
        return

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        stack = []
        cache = defaultdict(bool)
        nums = sorted(nums)
        for i in range(len(nums)):
            stack.append(nums[i])
            self.dfs(nums, i + 1, stack, result, cache)
            stack.pop()
        return result
```

시간 복잡도는 전체 배열 N 개라고 봤을 때, 자기 자신을 제외한 N-1 개에서 2개를 고르기 때문에
`N * ((N-1) * (N-2) / 2)` 인 것 같다. (?) 그러면 `O(N^3)` 이 맞나...?

### left, right 접근
전체 배열을 정렬한 후에, `현재 값 + 왼쪽 값 + 오른쪽 값` 을 비교 하여 0 이면 그 값을 결과 값에 추가, 0 보다 작으면 왼쪽에 해당하는 인덱스 증가, 
0 보다 크면 오른쪽에 해당하는 인덱스 감소 를 전체 N 번만큼 반복한다.

이미 정렬이 되어 있기 때문에 이전에 구했던 왼쪽 값이 연속해서 같은 수로 등장하는 경우 (예를 들면 [-3, -1, -1, -1, 0, 4] 와 같이 등장) 엔
-1 을 다시 계산할 필요가 없기 때문에 왼쪽 값이 달라질 때 까지 왼쪽 인덱스를 증가 시킨다. 오른쪽도 마찬가지로 감소 시킨다.

이렇게 전체 N 번만큼 인덱스를 증가 시키면서 N-1 개를 반복하여 left, right 를 비교하기 때문에 O(N^2) 으로 구현할 수 있다.

코드는 아래와 같다.

```python3
from collections import defaultdict


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        cache = defaultdict(bool)

        nums.sort()
        for i in range(len(nums) - 1):
            left, right = i + 1, len(nums) - 1
            while left < right:
                res = nums[i] + nums[left] + nums[right]
                if res < 0:
                    left += 1
                elif res > 0:
                    right -= 1
                else:
                    if (nums[i], nums[left], nums[right]) not in cache:
                        result.append([nums[i], nums[left], nums[right]])
                        cache[(nums[i], nums[left], nums[right])] = True
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return result
```
