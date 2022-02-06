# https://leetcode.com/contest/biweekly-contest-71/problems/partition-array-according-to-given-pivot/
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        less = []
        greater = []
        pivot_cnt = 0
        for num in nums:
            if num < pivot:
                less.append(num)
            elif num > pivot:
                greater.append(num)
            else:
                pivot_cnt += 1

        result = []
        for num in less:
            result.append(num)
        for _ in range(pivot_cnt):
            result.append(pivot)
        for num in greater:
            result.append(num)

        return result
