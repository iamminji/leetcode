# 621. Task Scheduler
# https://leetcode.com/problems/task-scheduler/


from typing import List
from collections import Counter, deque


class Solution:
    # task 들이 주어지고 쉬어야 할 시간 n 이 주어질 때 (같은 task는 반드시 n 만큼의 휴식시간이 필요하다)
    # 가장 적은 실행 시간을 리턴하는 문제다. (task 들을 효율적으로 우선순위를 정해서 실행하라는 의미)
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # 가장 많이 등장하는 task 가 먼저 실행되어야 하는 greedy 문제라고 볼 수 있다.
        # 그러나 사실 task 의 타입이 무엇인지는 알 필요가 없다.

        # 예를 들면 A, A, A, A, A, A, B, C, D, E, F, G 라는 task 가 오고 n 이 2라고 하자.
        # 실행시간을 단축시키려면 아무런 task도 진행할 수 없는 idle 시간을 단축시켜야 한다.
        # 즉 A idle idle A B C 보다는 A B C A 순서의 실행 시간이 더 적다는 의미다.
        # 결국엔 가장 많이 등장하는 task 는 먼저 실행되어야 하고 동시에 중간엔 최대한 다른 task 가 실행되게끔 해야 한다는 것이다.
        # 그러므로 task 의 종류 보다는 가장 많이 등장한 task 들을 빨리 소진 시킨다고 생각하면 된다.

        # 풀이는 아래와 같다.
        # 각 task 가 등장하는 횟수를 카운팅하고 이를 많이 등장하는 순서대로 정렬한다.
        counter = Counter(tasks)
        heap = sorted(counter.items(), key=lambda x: -x[1])
        # deque 는 양 쪽에서 pop을 할 수 있고 수행속도가 O(1)이라 바꿔 주었다.
        heap = deque(heap)

        execution_time = 0

        # task 가 남아 있는 동안 반복한다.
        while any(counter.keys()):
            i = 0
            # 쉬어야 할 시간 n 보다 현재 task 를 채운 시간 i 가 작아야 하고
            # 진행해야 할 task 가 남아 있을 때 까지 반복한다.
            while i <= n and any(counter.values()):
                if len(heap) > 0:
                    # 가장 많이 등장한 task 를 꺼낸다.
                    t, c = heap.popleft()
                    # 횟수를 차감시킨다.
                    counter[t] -= 1
                    if counter[t] == 0:
                        del counter[t]

                # 실행 시간을 추가한다.
                i += 1
                execution_time += 1

            # 남은 task 들을 다시 정렬한다.
            heap = sorted(counter.items(), key=lambda x: -x[1])
            heap = deque(heap)

        return execution_time

if __name__ == '__main__':
    # 덧붙이자면, 사실 파이썬에선 heapq 라는 자료구조가 있긴 하다.
    sol = Solution()
    assert sol.leastInterval(["A","A","A","B","B","B"], 2) == 8