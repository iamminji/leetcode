# 739. Daily Temperatures
# https://leetcode.com/problems/daily-temperatures/

from typing import List
from collections import deque


class Solution:
    # 숫자 리스트가 주어지고, 각 수보다 큰 다음 수의 인덱스를 구하는 문제다.
    def dailyTemperaturesTLE(self, T: List[int]) -> List[int]:
        """
        TLE
        :param T:
        :return:
        """

        # brute force 이고 TLE 뜸
        res = []
        for i, t1 in enumerate(T):
            j = i + 1
            while j < len(T):
                if t1 < T[j]:
                    break
                j += 1
            else:
                res.append(0)
                continue
            res.append(j - i)
        return res

    def dailyTemperatures(self, T: List[int]) -> List[int]:
        """
        AC
        :param T:
        :return:
        """

        # stack 을 이용해서 구했다.
        # 솔루션 참고 (https://leetcode.com/problems/daily-temperatures/solution/)
        # 꽤 어려운데 정답률이 40%가 넘어서 놀람

        res = [0 for _ in range(len(T))]
        i = len(T) - 1
        stack = deque()
        while i >= 0:
            while len(stack) > 0:
                # 현재 값이 스택의 값 보다 더 크면 스택에서 빼준다.
                # 찾아야 하는 것은 현재 값보다 커지는 값이기 때문이다.
                if T[i] >= T[stack[0]]:
                    stack.popleft()
                else:
                    break

            # 스택이 비어있지 않으면 가장 처음 스택에서 현재 인덱스를 빼준다.
            # 스택의 가장 첫번째 값이 현재 값에서 큰 바로 다음 값의 인덱스가 되기 때문이다.
            if stack:
                res[i] = stack[0] - i
            else:
                # 스택이 비어있다면 모든 스택을 다 뒤져봤다는 뜻이고 그러면 현재 값 보다 큰 값이 (현재 인덱스 보다 큰 인덱스에서) 없다는 의미
                # 그래서 0 을 넣어준다.
                res[i] = 0

            # 현재 인덱스를 스택에 새로 추가한다.
            # 리스트를 거꾸로 순회하므로 현재 인덱스는 이전 인덱스가 비교해야할 대상이 된다.
            stack.appendleft(i)
            i -= 1

        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.dailyTemperatures2([73, 74, 75, 71, 69, 72, 76, 73]))
