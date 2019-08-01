# 869. Reordered Power of 2
# https://leetcode.com/problems/reordered-power-of-2/

from itertools import permutations


class Solution:

    def reorderedPowerOf2(self, N: int) -> bool:
        # N 을 임의의 어떤 순서로 섞었을 때 해당 수가 2의 제곱근인지 판별하는 문제이다.
        # python 으로 brute force 하니 TLE 가 났다.

        # 우선 python 에서 제공하는 permutation 함수로 모든 순서쌍을 생성하였다. (TODO 직접 구현해볼것!)
        # 그리고 문제에서 주어지는 N은 10의 9승보다 작거나 같다고 했으므로 만약 2의 제곱승이 등장한다면 2의 29승이 최대가 될 것이다.
        # 참고: 2의 29승은 10자리이다

        # 그러므로 2의 1승부터 29승까지 모두 set 자료구조에 넣어주고,
        # N으로 만든 순서쌍 리스트의 어떤 값이 해당 자료구조에 존재하는지에 대한 여부를 리턴하면 된다.

        per = list(permutations(str(N)))
        nums = set()

        nums.add("1")
        nums.add("2")
        for i in range(2, 30):
            nums.add(str(2 << i))

        for p in per:
            if p[0] == "0":
                continue
            if "".join(p) in nums:
                return True

        return False
