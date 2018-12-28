# 801. Minimum Swaps To Make Sequences Increasing
# https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/description/


class Solution:
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """

        size = len(A)
        no_swap = [size for _ in range(size)]
        swap = [size for _ in range(size)]

        no_swap[0], swap[0] = 0, 1

        for i in range(1, len(A)):
            if A[i - 1] < A[i] and B[i - 1] < B[i]:
                no_swap[i] = no_swap[i - 1]
                swap[i] = swap[i - 1] + 1
            if A[i - 1] < B[i] and B[i - 1] < A[i]:
                no_swap[i] = min(no_swap[i], swap[i - 1])
                swap[i] = min(swap[i], no_swap[i - 1] + 1)

        return min(no_swap[-1], swap[-1])


if __name__ == "__main__":
    sol = Solution()
    # print(sol.minSwap([1, 3, 5, 4], [1, 2, 3, 7]))
    print(sol.minSwap([0, 7, 8, 10, 10, 11, 12, 13, 19, 18], [4, 4, 5, 7, 11, 14, 15, 16, 17, 20]))
    print(sol.minSwap([0, 4, 4, 5, 9], [0, 1, 6, 8, 10]))
