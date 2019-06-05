# 645. Set Mismatch
# https://leetcode.com/problems/set-mismatch/

from typing import List
from collections import Counter


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        count = Counter(nums)
        res = []
        i = 1
        dup = set()
        for n in nums:
            if count[n] == 2:
                if n not in dup:
                    res.append(n)
                dup.add(n)
            else:
                i += 1

        print(i, count)
        if i not in count:
            res.append(i)

        print(res)
        return res


if __name__ == '__main__':
    sol = Solution()
    assert sol.findErrorNums([1, 2, 2, 4]) == [2, 3]
    assert sol.findErrorNums([1, 1]) == [1, 2]
    assert sol.findErrorNums([2, 2]) == [2, 1]
