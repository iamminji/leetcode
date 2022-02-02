# 18. 4Sum
# https://leetcode.com/problems/4sum/

from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def threeSum(inums, itarget):
            result = []
            cache = set()
            for i in range(len(inums)):
                left = i + 1
                right = len(inums) - 1
                while left < right:
                    s = inums[left] + inums[right] + inums[i]
                    if s == itarget:
                        if (inums[i], inums[left], inums[right]) not in cache:
                            result.append([inums[i], inums[left], inums[right]])
                            cache.add((inums[i], inums[left], inums[right]))
                        left += 1
                        right -= 1
                    elif s < itarget:
                        left += 1
                    else:
                        right -= 1

            return result

        results = []
        nums.sort()
        for i in range(len(nums) - 1):
            if i == 0 or nums[i] != nums[i - 1]:
                threeResult = threeSum(nums[i + 1:], target - nums[i])
                for item in threeResult:
                    results.append([nums[i]] + item)
        return results


if __name__ == '__main__':
    sol = Solution()
    print(sol.fourSum([1, 0, -1, 0, -2, 2], 0))
    print(sol.fourSum([-3, -2, -1, 0, 1, 5], 0))
    print(sol.fourSum([2, 2, 2, 2, 2], 8))
    print(sol.fourSum([-2, -1, -1, 1, 1, 2, 2], 0))
