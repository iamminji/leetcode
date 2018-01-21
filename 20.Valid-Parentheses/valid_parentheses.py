# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/description/


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        closed_brackets = list()

        for ch in s:
            if ch == "(":
                closed_brackets.append(")")
            elif ch == "{":
                closed_brackets.append("}")
            elif ch == "[":
                closed_brackets.append("]")
            else:
                if not closed_brackets:
                    return False
                temp = closed_brackets.pop()
                if temp != ch:
                    return False

        return True if not closed_brackets else False


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid("["))
    print(sol.isValid("]"))
    print(sol.isValid("[(])"))
    print(sol.isValid("[()]"))
