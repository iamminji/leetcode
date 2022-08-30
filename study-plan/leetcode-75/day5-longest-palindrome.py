# https://leetcode.com/problems/longest-palindrome/
# 409. Longest Palindrome

from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)

        result = 0
        for k, v in counter.items():
            if v % 2 == 0:
                result += v
                counter[k] = 0
            elif v % 2 != 0 and v >= 2:
                result += v - 1
                counter[k] -= 1

        for k, v in counter.items():
            if v > 0:
                result += 1
                break
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestPalindrome("abccccdd"))
    print(sol.longestPalindrome("a"))
