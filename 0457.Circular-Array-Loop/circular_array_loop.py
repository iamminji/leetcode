# 457. Circular Array Loop
# https://leetcode.com/problems/circular-array-loop/


class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        idx = 0
        pos_idx_list = [i for i in range(0, len(nums) - 1)]
        neg_idx_list = [-i for i in range(len(nums), 0, -1)]
        while idx < len(nums):
            new_idx = nums[idx] + idx
            if new_idx > 0:
                if new_idx % len(nums) not in pos_idx_list:
                    return False
            else:
                if new_idx % len(nums) not in neg_idx_list:
                    return False
            idx = new_idx
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.circularArrayLoop([2, -1, 1, 2, 2]))
    print(sol.circularArrayLoop([-1, 2]))
    print(sol.circularArrayLoop([]))
    print(sol.circularArrayLoop([1]))
    print(sol.circularArrayLoop([-2, 1, -1, -2, -2]))
