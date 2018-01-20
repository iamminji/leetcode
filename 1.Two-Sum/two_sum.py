# 1. Two Sum
# https://leetcode.com/problems/two-sum/description/


from collections import defaultdict


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_map = defaultdict(list)

        for idx, num in enumerate(nums):
            nums_map[num].append(idx)

        result = list()

        for num, idx_list in nums_map.items():
            if len(idx_list) == 1:
                if target - num in nums_map:
                    return [idx_list[0], nums_map[target - num][0]]
            else:
                for i in idx_list:
                    if target - nums[i] in nums_map or target - nums[i] == 0:
                        result.append(i)
                        target -= nums[i]
                    else:
                        break

        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([3, 2, 4], 6))
    print(sol.twoSum([1, 2, 4], 5))
    print(sol.twoSum([3, 3], 6))
