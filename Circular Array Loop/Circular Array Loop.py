# You are given an array of positive and negative integers. If a number n at an index is positive, then move forward n steps. Conversely, if it's negative (-n), move backward n steps. Assume the first element of the array is forward next to the last element, and the last element is backward next to the first element. Determine if there is a loop in this array. A loop starts and ends at a particular index with more than 1 element along the loop. The loop must be "forward" or "backward'.
#
# Example 1: Given the array [2, -1, 1, 2, 2], there is a loop, from index 0 -> 2 -> 3 -> 0.
#
# Example 2: Given the array [-1, 2], there is no loop.
#
# Note: The given array is guaranteed to contain no element "0".
#
# Can you do it in O(n) time complexity and O(1) space complexity?

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
