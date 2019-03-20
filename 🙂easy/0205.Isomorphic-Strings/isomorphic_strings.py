# 205. Isomorphic Strings
# https://leetcode.com/problems/isomorphic-strings/


class Solution:
    # 주어진 문자열 s와 t가 같은 모양(isomorphic) 인지 판별하는 문제다.
    def isIsomorphic(self, s: str, t: str) -> bool:

        # 문자열 길이 비교
        if len(s) != len(t):
            return False

        # 문자열 매치 딕셔너리를 만든다.
        d = dict()

        # s에 있는 문자와 t의 문자를 비교하여 달라지면 바로 False를 리턴한다.
        for x1, x2 in zip(s, t):
            if x1 not in d:
                d[x1] = x2
            else:
                if d[x1] != x2:
                    return False

        d2 = dict()
        # 반대 경우도 확인한다.
        for x1, x2 in zip(t, s):
            if x1 not in d2:
                d2[x1] = x2
            else:
                if d2[x1] != x2:
                    return False

        return True


if __name__ == '__main__':
    sol = Solution()
    assert sol.isIsomorphic("egg", "add") == True
    assert sol.isIsomorphic("foo", "bar") == False
    assert sol.isIsomorphic("paper", "title") == True
    assert sol.isIsomorphic("ab", "aa") == False
