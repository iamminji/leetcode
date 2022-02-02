# 80. Remove Duplicates from Sorted Array II
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        res = len(nums)
        i = 0
        j = 1
        k = 2
        while k < len(nums) and k < res:
            if nums[i] == nums[j] == nums[k]:
                # reorder
                for p in range(k, len(nums) - 1):
                    nums[p] = nums[p + 1]
                res -= 1
            elif nums[i] == nums[j] and nums[j] != nums[k]:
                i = k
                j = i + 1
                k += 2
            else:
                i += 1
                j += 1
                k += 1

        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3]))
    print(sol.removeDuplicates([1, 1, 1, 2, 2, 3]))
