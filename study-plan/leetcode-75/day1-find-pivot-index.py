# https://leetcode.com/problems/find-pivot-index/
# 724. Find Pivot Index
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            if left_sum == (total - nums[i] - left_sum):
                return i
            left_sum += nums[i]
        return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.pivotIndex([1, 7, 3, 6, 5, 6]))
    print(sol.pivotIndex([1, 2, 3]))
    print(sol.pivotIndex([2, 1, -1]))
    # 사실 아래 케이스에서는 안돌아가는데 코드는 통과가 됨...
    # https://leetcode.com/problems/find-pivot-index/discuss/136167/This-is-a-very-poorly-described-problem
    print(sol.pivotIndex([-1, -1, -1, 0, 1, 1]))
