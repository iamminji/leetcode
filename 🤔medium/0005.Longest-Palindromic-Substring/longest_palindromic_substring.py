# 5. Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/


class Solution:

    def longestPalindrome2(self, s: str) -> str:
        if len(s) <= 1:
            return s

        # Time Complexity O(n^2)
        # O(n^3) 을 나눈 것과 같다. 기존에는 맨 마지막 인덱스를 감소시키면서 문자열 전체가 palindrome 한지 보았다면
        # 이번에는 글자 단위로 같은지 확인한다.
        # 두 번에 나눠서 진행한 이유는 abba, aba 와 같이 palindrome이 짝수/홀수 인 경우가 있기 때문이다.
        res = ""
        for i in range(len(s)):

            start, end = i, i
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1

            if len(s[start + 1:end]) > len(res):
                res = s[start + 1:end]

            start, end = i, i + 1
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1

            if len(s[start + 1:end]) > len(res):
                res = s[start + 1:end]

        return res

    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        # Time Complexity O(n^3)
        # 맨 마지막 부터 시작 지점까지 인덱스를 감소시키면서 현재 문자열이 palindrome 인지 본다.
        # palindrome 인지 확인하기 위한 함수가 O(n) 이라 전체 시간 복잡도는 O(n^3) 이다.
        pos = 1
        res = s[0]
        for i in range(len(s)):
            for j in range(len(s), i, -1):
                if s[i:j] == s[i:j][::-1]:
                    if pos <= j - i + 1:
                        pos = j - i + 1
                        res = s[i:j]
                    break
        return res
