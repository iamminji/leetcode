# https://leetcode.com/contest/weekly-contest-279/problems/smallest-value-of-the-rearranged-number/
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = list()
        odd = list()
        for i, num in enumerate(nums):
            if i % 2 == 0:
                even.append(num)
            else:
                odd.append(num)

        even.sort()
        odd.sort()
        odd.reverse()

        result = []
        o, e = 0, 0
        for i in range(len(nums)):
            if i % 2 != 0:
                result.append(odd[o])
                o += 1
            else:
                result.append(even[e])
                e += 1
        return result
