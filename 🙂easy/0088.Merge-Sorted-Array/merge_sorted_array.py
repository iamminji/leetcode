# 88. Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/

from typing import List


class Solution:
    # 정렬된 두 개의 리스트를 하나로 합치는 문제
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # O(n^2*logn) 으로 일단 풀어봄
        # todo O(n) 으로 바꿔보자
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if i >= m:
                nums1[i] = nums2[j]
                i += 1
                j += 1
            elif nums1[i] <= nums2[j]:
                i += 1
            else:
                nums1[i], nums2[j] = nums2[j], nums1[i]

            nums2 = sorted(nums2)
