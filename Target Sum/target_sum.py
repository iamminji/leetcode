# 494. Target Sum
# https://leetcode.com/problems/target-sum/


class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """

        self.count = 0
        self.solution(0, nums, 0, S, len(nums)-1)
        return self.count

    def solution(self, idx, nums, cur, S, length):

        if idx == length+1:
            if cur == S:
                self.count += 1
            return
        self.solution(idx+1, nums, cur+nums[idx], S, length)
        self.solution(idx+1, nums, cur-nums[idx], S, length)

if __name__ == '__main__':
    sol = Solution()
    print sol.findTargetSumWays([1,1,1,1,1], 3)
    print sol.findTargetSumWays([1,2,3,4], 6)
    print sol.findTargetSumWays([1,0], 1)
    print sol.findTargetSumWays([42,24,30,14,38,27,12,29,43,42,5,18,0,1,12,44,45,50,21,47], 38)
