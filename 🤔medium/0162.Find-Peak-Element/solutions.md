## 문제 설명
숫자 배열에서 peak (꼭짓점) 을 찾는 문제다.

문제에서 배열의 길이는 나와 있지 않고, `Your solution should be in logarithmic complexity.` 라고 되어있다.

## 솔루션

### 선형으로 풀기
인덱스 3개 이용해서 꼭짓점을 아래와 같이 구했다. 이런 문제들의 엣지 포인트는 오름차순으로 배열이 되어있던가, 내림차순으로 되어 있던가 하는 문제다.
이런 예제들은 인덱스 3개로 순회해서 구할 수는 없어서 기울기를 따로 계산했다. 

while 문 안에서 꼭짓점을 찾으면 리턴하고, 이 때 찾지 못했을 경우
기울기 값이 음수면 그 배열은 내림차순으로만 되어 있으므로 가장 값(mx) 가 컸던 인덱스 (mxi) 를 아니면 가장 마지막 지점 두 개 중 큰 값을 리턴하게 했다.

```python3
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        i = 0
        k = 0
        mx = -1
        mxi = 0

        if len(nums) == 1:
            return 0

        if len(nums) == 2:
            if nums[0] < nums[1]:
                return 1
            return 0

        while i < len(nums) - 2:
            if nums[i] < nums[i + 1] and nums[i + 2] < nums[i + 1]:
                return i + 1
            k = nums[i + 1] - nums[i]
            if nums[i] > mx:
                mx = nums[i]
                mxi = i
            i += 1

        if k > 0:
            if nums[i] < nums[i + 1]:
                return i + 1
            return i
        else:
            return mxi
```

### 로그로 풀기
`Your solution should be in logarithmic complexity.` 라고 문제에 적혀 있었다. 로그의 시간 복잡도면 binary search 일 것 같았다.

```python3
class Solution:
    def recursive(self, nums, start, end):
        if end - start == 1:
            if nums[start] < nums[end]:
                return end
            return start

        mid = (start + end) // 2

        left = self.recursive(nums, start, mid)
        right = self.recursive(nums, mid, end)

        if nums[left] < nums[right]:
            return right
        return left

    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        return self.recursive(nums, 0, len(nums) - 1)
```

binary search 로 값이 큰 쪽으로 인덱스를 확장 시켰더니 되더라(?)


## 주저리
[솔루션](https://leetcode.com/problems/find-peak-element/solution/)을 보니까... 같은 알고리즘이여도 엄청 짧아서 충격 먹음 ㅜ