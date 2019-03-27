# 9. Palindrome Number
# https://leetcode.com/problems/palindrome-number/


class Solution:
    # 주어진 숫자가 회문인지 판별하는 문제다.
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


if __name__ == '__main__':
    # 1년전에 풀었는데 풀이를 보니 다시 푼 것과 코드가 완전히 일치했다.
    # 놀라운 점은 코드는 같은데 걸린 시간 7배 빨라졌다. LeetCode.. 살림 살이 많이 펴진듯

    # easy/0007 번 문제와 같이 문자열로 풀지 말고 integer로 활용해 풀어야했던 문제인듯 싶다.
    sol = Solution()
    assert sol.isPalindrome(123) == False
