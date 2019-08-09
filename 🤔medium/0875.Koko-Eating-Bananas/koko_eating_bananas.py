# 875. Koko Eating Bananas
# https://leetcode.com/problems/koko-eating-bananas/


class Solution:

    def canEat(self, k, piles, h):

        t = 0
        for pile in piles:
            if pile % k != 0:
                t += 1
            t += pile // k

        return t <= h

    def minEatingSpeed(self, piles: 'List[int]', H: 'int') -> 'int':

        # koko 가 바나나를 전부 먹을 수 있는 최소 시간을 찾는 문제다.
        # koko 는 piles[i] 가 전부 먹을 수 있는 최소 시간 K 보다 작거나 같으면 i 번째 바나나를 다 먹을 수 있다.
        # 만약 piles[i] > K 라면 koko 는 시간을 더 써야 한다.

        # 이를 canEat 에 구현하였다.
        # 나머지가 0 이면 몫 만큼 시간을 쓴 것이고 나머지가 생기면 +1 을 더 해준다.

        # 그리고 구해야할 최소 시간은 바이너리 서치로 구하면 된다.
        # koko 가 어떤 K 시간 안에 바나나를 다 먹을 수 있다면 정답은 K 보다 더 작아질 수 있다. (연속된 해를 갖고 있음)
        # 이를 이진 탐색으로 구하는 것이다.
        # 그리고 구해야할 값은 최소값이므로 lo 를 리턴하면 된다.

        lo = 1
        hi = max(piles)

        while lo <= hi:
            k = (lo + hi) // 2
            if self.canEat(k, piles, H):
                hi = k - 1
            else:
                lo = k + 1

        return lo
