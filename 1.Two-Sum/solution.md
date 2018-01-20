#### 문제 풀이

[Two Sum](https://leetcode.com/problems/two-sum/) 라는 문제다
난이도는 **Easy** 이고 추천 수가 높은 문제다.

주어진 target과 배열이 있고, 해당 target은 주어진 배열의 두 원소의 값을 합한 것과 같다고 가정 했을 때(이 때 항상 값이 존재할 뿐만 아니라 정답은 언제나 하나라고 가정하고 있다.),
 두 원소의 인덱스 값이 담겨진 리스트를 리턴하는 문제다.
 
문제에서 예외들을 모두 가정하였고 리스트에 담길 원소의 값이 2개라고 정해져있기 때문에, 가장 먼저 시도했던 것은 for loop를 두 번 쓰는 것이었다.
코드는 다음과 같다.

<pre><code>
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        res = list()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    res.append(i)
                    res.append(j)
                    break

        return res
</code></pre>

예전에 Golang으로 풀어본 적이 있는데, Accepted 되었기 때문에 무리 없이 정답 처리가 될 거라고 생각하였지만, <pre>Time Limit Exceeded</pre> 가 떴다

그리하여, 문제 접근을 다르게 하였는데 두 번째 방법은 Map(Python에선 Dictionary)를 쓰는 것이었고 Accepted 되었다.
.
방법은 다음과 같다.
1. 먼저 map 에 Key로는 num(수)을 넣고 Value로는 index list를 넣는다. (이 때 index가 아닌 리스트를 넣는 이유는 같은 원소의 값이 여러개 나올 수도 있기 때문이었다.)
2. 그리고 해당 map을 순회하면서 target에서 Key인 num을 뺀 값이 map에 있는지 찾아보고, 있으면 현재 index와 target-num 의 index 두 값이 담긴 리스트를 리턴 해주었다.

기본 아이디어는 이렇고, 예외로 같은 값이 여러개가 있는 리스트가 있을 경우 index list의 길이가 1 보다 클 것이기 때문에 그 부분만 따로 else 분기로 한 번 더 for loop를 돌렸다.
(예제 입력값으로 target이 3이고, nums가 [3,3]인 경우를 생각해보면 될 것 같다.)

시간 복잡도는 O(n)이고 공간 복잡도도 O(n)이다.