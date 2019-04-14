# 1021. Remove Outermost Parentheses
# https://leetcode.com/problems/remove-outermost-parentheses/


class Solution(object):
    # 가장 바깥의 괄호를 없애는 문제다.
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """

        # open, close 괄호 개수를 비교하여 개수가 같으면 초기화 한다.
        # 단, 처음에 open 괄호가 나오면 무시한다.
        o, c = 0, 0
        res = ""
        for b in S:
            if b == "(":
                o += 1
            else:
                c += 1
            if o == c:
                o = 0
                c = 0
                continue
            if o == 1:
                continue
            res += b

        return res
