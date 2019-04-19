# 670. Maximum Swap
# https://leetcode.com/problems/maximum-swap/
from copy import copy


class Solution:
    # 한번 교환하여 주어진 숫자에서 최대값을 만들어 리턴하는 문제다.

    def maximumSwap(self, num: int) -> int:
        # brute force 로 O(n^2) 하였다.
        # 숫자가 1억까지 온대서 안될 줄 알았는데 됨
        nums = list(str(num))
        res = copy(nums)

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                if int("".join(nums)) > int("".join(res)):
                    res = copy(nums)
                nums[i], nums[j] = nums[j], nums[i]

        return int("".join(res))

    def maximumSwap2(self, num):
        # 숫자를 위 처럼 문자열 리스트로 바꾼 후 해당 수를 키로 값을 등장한 인덱스로 넣어주었다.
        # 문제에서 주어진 swap 은 단 한번이고 이를 이용해 제일 큰 수를 만들어야 하므로 가장 큰 자릿수와 가장 작은 자릿수 끼리 비교하여
        # 가장 작은 자릿수의 수가 큰 자릿수의 수 보다 크면 두 수를 바꿔치기 했다.

        # 중간에 정렬도 하고 반복문으로도 돌지만 실제 해당 딕셔너리는 0~9 까지만 키로 갖고 있으므로 시간 복잡도는 O(n) 이다.

        nums = list(str(num))
        d = dict()

        for i, n in enumerate(nums):
            if n not in d:
                d[n] = i
            else:
                d[n] = max(d[n], i)

        sd = sorted(d, reverse=True)
        for i, n in enumerate(nums):
            for n2 in sd:
                if n2 > n and d[n2] > i:
                    nums[i], nums[d[n2]] = nums[d[n2]], nums[i]
                    return int("".join(nums))

        return int("".join(nums))


if __name__ == '__main__':
    sol = Solution()
    assert sol.maximumSwap(2736) == 7236
    assert sol.maximumSwap(9973) == 9973
