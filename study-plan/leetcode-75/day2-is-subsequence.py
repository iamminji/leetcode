# https://leetcode.com/problems/is-subsequence/
# 392. Is Subsequence

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1

        return i == len(s)


if __name__ == '__main__':
    sol = Solution()
    print(sol.isSubsequence("abc", "ahbgdc"))
    print(sol.isSubsequence("axc", "ahbgdc"))
    print(sol.isSubsequence("b", "abc"))
