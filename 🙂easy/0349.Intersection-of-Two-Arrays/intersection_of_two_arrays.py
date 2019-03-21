# 349. Intersection of Two Arrays
# https://leetcode.com/problems/intersection-of-two-arrays/

class Solution:
    # nums1 과 nums2 의 교집합을 구하는 문제다.
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))
