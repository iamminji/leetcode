# 35. Search Insert Position
# https://leetcode.com/problems/search-insert-position/


class Solution:
    # 정렬된 리스트가 주어질 때 target 이 존재해야할 인덱스를 리턴하는 문제다.
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # 리스트는 이미 정렬되어 있기 때문에 이터레이터를 돌면서 num이 target 보다 크면 해당 인덱스를 리턴한다.
        for idx, num in enumerate(nums):
            if num >= target:
                return idx

        return len(nums)
