# 551. Student Attendance Record I
# https://leetcode.com/problems/student-attendance-record-i/#/description


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = [x == "L" for x in s]
        return not (s.count("A") >= 2 or any(map(ll, l, l[1:], l[2:])))


def ll(x, y, z):
    return x and y and z
