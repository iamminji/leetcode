# 941. Valid Mountain Array
# https://leetcode.com/problems/valid-mountain-array/


class Solution:
    def validMountainArray(self, A: 'List[int]') -> 'bool':
        asc = False
        desc = False
        for i in range(1, len(A)):
            if A[i - 1] < A[i]:
                if not desc:
                    asc = True
                else:
                    return False
            elif A[i - 1] > A[i]:
                if asc:
                    desc = True
                else:
                    return False
            else:
                return False
        return asc and desc
