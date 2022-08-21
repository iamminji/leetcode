# 2384. Largest Palindromic Number
# https://leetcode.com/problems/largest-palindromic-number/

from collections import Counter, deque


class Solution:
    def largestPalindromic(self, num: str) -> str:

        if not num:
            return ""

        counter = Counter(num)
        result = deque()

        stack = list("9876543210")
        while stack:
            c = stack.pop()
            value = counter[c]
            while value > 1:
                result.append(c)
                result.appendleft(c)
                value -= 2
            counter[c] = value

        mid = len(result) // 2

        stack = list("0123456789")
        while stack:
            c = stack.pop()
            value = counter[c]
            if value == 1:
                result.insert(mid, c)
                break

        while len(result) >= 2:
            if result[0] != "0":
                break
            result.pop()
            result.popleft()

        # 여기까지 왔는데 result 값이 없다는 얘기는
        # 남은게 0 짝수밖에 없다는 얘기임
        if not result:
            return "0"
        return "".join(result)


if __name__ == '__main__':
    sol = Solution()
    print(sol.largestPalindromic("444947137"))
    print(sol.largestPalindromic("00000"))
    print(sol.largestPalindromic("000000"))
    print(sol.largestPalindromic("00009"))
    print(sol.largestPalindromic("00001105"))
