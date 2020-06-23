# 287. Find the Duplicate Number
# https://leetcode.com/problems/find-the-duplicate-number/

from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = nums[0]
        hare = nums[nums[0]]

        # 사이클 찾기
        # 문제에서 무조건 duplicate number 가 있다고 했기 때문에 사이클은 무조건 된다.
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]

        # 사이클의 시작 지점을 찾는다
        tortoise = 0
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return hare


if __name__ == '__main__':
    sol = Solution()
    print(sol.findDuplicate([4, 3, 1, 4, 2]))
    print(sol.findDuplicate([1, 3, 4, 2, 2]))
