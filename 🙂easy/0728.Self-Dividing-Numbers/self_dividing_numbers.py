# 728. Self Dividing Numbers
# https://leetcode.com/problems/self-dividing-numbers/description/


class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """

        result = list()
        for i in range(left, right + 1):
            nums = str(i)
            for n in nums:
                if n == '0':
                    break
                if i % int(n) != 0:
                    break
            else:
                result.append(i)

        return result
