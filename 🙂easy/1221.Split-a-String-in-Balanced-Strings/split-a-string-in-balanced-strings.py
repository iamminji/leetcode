# 1221. Split a String in Balanced Strings
# https://leetcode.com/problems/split-a-string-in-balanced-strings/


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result = 0
        lc = 0
        rc = 0

        for st in list(s):
            if st == "L":
                lc += 1
            else:
                rc += 1
            if lc == rc:
                result += 1

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.balancedStringSplit("RLRRLLRLRL"))
    print(sol.balancedStringSplit("RLRRRLLRLL"))
    print(sol.balancedStringSplit("LLLLRRRR"))
