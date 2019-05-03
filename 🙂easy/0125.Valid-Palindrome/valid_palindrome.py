# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/


class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = [c.lower() for c in s if c.isalnum()]
        return c == c[::-1]
