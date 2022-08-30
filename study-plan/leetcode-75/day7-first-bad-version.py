# https://leetcode.com/problems/first-bad-version/
# 278. First Bad Version

# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    return version == 1702766719


class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            if not isBadVersion(mid):
                left = mid + 1
            else:
                right = mid - 1

        return left


if __name__ == '__main__':
    sol = Solution()
    print(sol.firstBadVersion(2126753390))
