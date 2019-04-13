# 922. Sort Array By Parity II
# https://leetcode.com/problems/sort-array-by-parity-ii/


class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        res = [0 for _ in range(len(A))]

        i, j = 0, 1
        for n in A:
            if n % 2 == 0:
                res[i] = n
                i += 2
            else:
                res[j] = n
                j += 2

        return res
