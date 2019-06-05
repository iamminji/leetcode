# 45. Jump Game II
# https://leetcode.com/problems/jump-game-ii/


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tail = 0
        head = 0
        cnt = 0
        for idx in range(len(nums)):
            if idx > tail:
                cnt += 1
                tail = head
            head = max(head, idx + nums[idx])
        return cnt

