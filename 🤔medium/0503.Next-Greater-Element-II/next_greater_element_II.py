# 503. Next Greater Element II
# https://leetcode.com/problems/next-greater-element-ii/

from typing import List


class Solution:

    # TODO Stack 으로도 풀어보기
    def nextGreaterElementsStack(self, nums: List[int]) -> List[int]:
        pass

    # TOO SLOW!
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        cur_idx, idx = 0, 1
        size = len(nums)
        ans = [-1 for _ in range(size)]

        while cur_idx < size:
            if nums[cur_idx] < nums[idx % size]:
                ans[cur_idx] = nums[idx % size]
                cur_idx += 1
                idx = cur_idx + 1
            else:
                # 되돌아옴
                if cur_idx == (idx % size):
                    cur_idx += 1
                else:
                    idx += 1

        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.nextGreaterElements([100, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
    print(sol.nextGreaterElements([100, 10, 9]))
    print(sol.nextGreaterElements([1, 2, 1]))
    print(sol.nextGreaterElements([1, 2, 3, 4, 3]))
