from typing import List
from collections import defaultdict


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        cache = defaultdict(bool)

        nums.sort()
        for i in range(len(nums) - 1):
            left, right = i + 1, len(nums) - 1
            while left < right:
                res = nums[i] + nums[left] + nums[right]
                if res < 0:
                    left += 1
                elif res > 0:
                    right -= 1
                else:
                    if (nums[i], nums[left], nums[right]) not in cache:
                        result.append([nums[i], nums[left], nums[right]])
                        cache[(nums[i], nums[left], nums[right])] = True
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

        return result


if __name__ == '__main__':
    m = [-1, 0, 1, -12, 12]
    sol = Solution()
    print(sol.threeSum(m))
    m2 = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
    # print(sol.threeSum(m2))
    m3 = [-13, 11, 11, 0, -5, -14, 12, -11, -11, -14, -3, 0, -3, 12, -1, -9, -5, -13, 9, -7, -2, 9, -1, 4, -6, -13, -7,
          10, 10, 9, 7, 13, 5, 4, -2, 7, 5, -13, 11, 10, -12, -14, -5, -8, 13, 2, -2, -14, 4, -8, -6, -13, 9, 8, 6, 10,
          2, 6, 5, -10, 0, -11, -12, 12, 8, -7, -4, -9, -13, -7, 8, 12, -14, 10, -10, 14, -3, 3, -15, -14, 3, -14, 10,
          -11, 1, 1, 14, -11, 14, 4, -6, -1, 0, -11, -12, -14, -11, 0, 14, -9, 0, 7, -12, 1, -6]
    # print(sol.threeSum(m3))
    m4 = [0, 0, 0]
    # print(sol.threeSum(m4))
    m5 = [3, 0, -2, -1, 1, 2]
    # print(sol.threeSum(m5))
    m6 = [-15, 10, 0, -2, 14, -1, -10, -14, 10, 12, 6, -6, 10, 2, -11, -9, 2, 13, 2, -9, -14, -12, -10, -12, 13, 13,
          -10, -3, 2, -11, 3, -6, 6, 10, 7, 5, -13, 4, -2, 12, 1, -11, 14, -4, 6, -12, -6, -14, 8, 11, -8, 1, 7, -3, 5,
          5, -13, 10, 9, -3, 6, -10, 6, -3, 7, -9, -13, 9, 10, 0, -1, -11, 4, -10, -8, -13, -15, 2, -12, 8, -2, -12,
          -14, -10, -8, 6, 2, -5, -7, -11, 7, 14, -6, -10, -12, 8, -4, -10, -5, 14, -3, 9, -12, 8, 14, -13]
    # print(sol.threeSum(m6))
    m7 = [-5, 1, -10, 2, -7, -13, -3, -8, 2, -15, 9, -3, -15, 13, -6, -10, 5, 6, 11, 1, 13, -12, 14, 6, 11, 4, 13, -14,
          0, 11, 1, 10, -11, 6, -11, -10, 8, 2, -3, -13, -6, -9, -9, -6, 11, -8, -9, 1, 13, 9, 9, 3, 13, 0, -6, 1, -10,
          -15, 3, 5, 3, 11, -8, 0, 2, -11, 5, -13, 6, 9, -11, 7, 8, -13, 8, 4, -6, 14, 13, -15, 1, 7, -5, -1, -7, 5, 7,
          -2, -3, -13, 10, 7, 13, 9, -8, -8, 13, 12, -6, 4, 7, -10, -12, -8, -8, 11, 11, -6, 3, 9, -14, -11, 2, -4, -5,
          10, 8, -13, -7, 12, -10, 10]
    print(sol.threeSum(m7))
