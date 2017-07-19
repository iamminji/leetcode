# 643. Maximum Average Subarray I
# https://leetcode.com/problems/maximum-average-subarray-i/#/description


class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        
        res = sum(nums[:k])
        tmp = res
        s_idx = 0
        for idx in range(1, len(nums)):
            if idx + k > len(nums):
                break
            tmp = tmp + nums[s_idx+k] - nums[s_idx]
            res = max(res, tmp)
            s_idx = idx
        
        return float(res) / float(k)
