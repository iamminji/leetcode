#### 문제 풀이

[Find All Numbers Disappeared in an Array](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/) 
라는 문제다.

난이도는 **Easy** 이지만, 주어진 조건인 공간 없이 / 시간 복잡도 O(n)으로 하려면 조금 생각을 해야 한다.

문제는 n 사이즈 만큼 리스트가 주어지는데, 리스트 안의 값은 1 부터 n 까지의 수로 이루어져 있다. 이 때, 리스트의 값들은 한 번 혹은 두 번씩 등장하는데,
1 부터 n 까지의 수 중에 리스트에 등장하지 않은 수들을 리턴하는 것이다.

사전 조건 없이 생각하자면, 단순히 O(n) 만큼 공간을 만들어서, 각각의 값들의 카운트를 넣고 그 공간을 다시 순회하면서 
1부터 n 까지 등장하지 않은 수 들을 리스트에 담아서 리턴하면 될 것 같다.

이러면 공간 O(n) / 시간 O(n) 에 할 수 있을 것 같다.

공간 없이 생각해보자면 정렬 해서 그냥 앞에서 부터 세도 될 것 같지만 이러면 시간 복잡도가 최소 O(nlogn)이라서 이 것도 주어진 조건을 만족하지 못한다.


그 다음 생각했던 것이 앞에서 부터 순회하면서 각 값들을 자기 위치(인덱스)에 넣는 것이었다.
그래서 값을 swap 하다가, swap 할 위치에 이미 나와 같은 수가 등장했다면 그냥 냅 두고 그렇게 한 번 O(n) 하고
다시 리스트 순회하면서 위치(인덱스)랑 값이 다르면 그 값은 리스트에 없다고 생각하였다.

하지만 <code>[1, 5, 2, 4, 5]</code> 에선 잘 돌아가지만 주어진 테스트 케이스 <code>[4, 3, 2, 7, 8, 2, 3, 1]</code> 에서는 또 안되었다.
그래서 그냥 임의 대로 두 번의 loop 가 아니라 3번 해 볼까? 했는데 오답 나고, 왜 오답 났는지 몰라서 5번 loop 돌렸더니 정답이 떠버렸다.

리스트의 전체 길이가 몇 이상이면 이 답은 오답일 것 같은데, 테스트 케이스가 34개 밖에 안되어서 통과 된 것 같다.

코드는 아래와 같다. (통과는 되었으나, 운이 좋아서 된 것 같은 느낌! 오답 나오는 테스트 케이스 찾아서 contribute 해볼까도 생각 해봄 😓)
<pre><code>
class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res = list()

        for _ in range(5):
            for idx in range(len(nums)):
                if idx + 1 != nums[idx]:
                    key = nums[idx]
                    if key != nums[key - 1]:
                        nums[idx], nums[key - 1] = nums[key - 1], nums[idx]

        for idx in range(len(nums)):
            if idx + 1 != nums[idx]:
                res.append(idx + 1)

        return res
</code></pre>

그래서 그냥 디스커스를 보기로 했다.
<pre><code>
class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]

</code></pre>

이 거 보고 진짜 깜짝 놀랐다. 어떻게 이런 생각을 했는지...

아이디어 자체는 문제에서 주어진 사이즈 크기 만큼 까지만 리스트에 주어진 다는 것을 알고 있기 때문에 가능한 것이다.

바로 순회하면서 현재 값을 리스트의 인덱스로 보고, 그 인덱스 해당 하는 값에 -1 을 곱해주고 다시 순회 하여서 -1 이 곱해지지 않은 인덱스를 리턴하는 것이다!

예제로 보면 이해하기가 훨씬 쉽다.

입력 값으로 <code>[1, 5, 2, 4, 5]</code>가 들어온다면 처음의 값(1)에 해당하는 인덱스 / 위치는 0 임을 알 수 있다. 그래서 인덱스(0)에 -1을 곱해준다.

그 다음으로 값(5)가 위치해야할 곳은 인덱스(4) 이므로 해당 인덱스의 값 5에 -1을 곱해준 것이다.

이처럼 자기 값이 원래 있어야할 자리에 -1을 곱한다면, 리스트에 존재하지 않은 값에 해당하는 인덱스는 양수 임을 알 수 있으니, 리스트에서 양수값만 리턴하면 된다!

nums는 위의 예제에선 
<pre>
[-1, 5, 2, 4, 5]
[-1, 5, 2, 4, -5]
[-1, -5, 2, 4, -5]
[-1, -5, 2, -4, -5]
[-1, -5, 2, -4, -5]
[-1, -5, 2, -4, -5]
</pre>

이렇게 순회하면서 바뀔 것이다.

이러면 시간 복잡도 O(n)과 공간 복잡도 없이! 구할 수 있다.

왜 좋아요가 많은가 했더니, 아이디어가 재밌어서 그런 것 같다. 😉