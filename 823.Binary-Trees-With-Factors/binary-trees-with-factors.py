# 823. Binary Trees With Factors
# https://leetcode.com/problems/binary-trees-with-factors/description/


class Solution:
    def numFactoredBinaryTrees(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A = sorted(A)
        dp = dict()

        for i in range(len(A)):
            dp[A[i]] = 1
            for j in range(i):
                if A[i] % A[j] == 0 and A[i] // A[j] in dp:
                    dp[A[i]] += (dp[A[j]] * dp[A[i] // A[j]])
        return sum(dp.values()) % (10 ** 9 + 7)


if __name__ == "__main__":
    sol = Solution()
    print(sol.numFactoredBinaryTrees([2, 4]))
    print(sol.numFactoredBinaryTrees([2, 4, 5, 10]))
    print(sol.numFactoredBinaryTrees([2, 4, 8]))
