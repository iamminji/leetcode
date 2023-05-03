# https://leetcode.com/problems/first-bad-version/description/
# 278. First Bad Version


# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        start, end = 1, n
        result = float("inf")

        while start <= end:
            mid = (start + end) // 2
            if not isBadVersion(mid):
                start = mid + 1
            else:
                result = min(result, mid)
                end = mid - 1
        return result


def isBadVersion(version) -> bool:
    # 이미 Leetcode가 구현해서 구현할 필요가 없음
    # 런타임 에러 때문에 만들어둠
    pass
