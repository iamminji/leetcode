# 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/

from typing import List


class Solution:
    # 문자열 리스트에서 가장 긴 prefix 를 찾는 문제다.
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # 문자열을 제일 긴 순서대로 정렬해서 전체 순회하여 가장 긴 prefix 를 찾았다.
        strs = sorted(strs, key=lambda x: len(x), reverse=True)

        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return strs[0]

        prefix = strs[0]
        for i in range(1, len(strs)):
            p, q = 0, 0
            res = ""
            while p < len(prefix) and q < len(strs[i]) and prefix[p] == strs[i][q]:
                res += prefix[p]
                p += 1
                q += 1

            if res != "":
                prefix = res
            else:
                return ""

        return prefix


if __name__ == '__main__':
    sol = Solution()
    assert sol.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
    assert sol.longestCommonPrefix(["a", "a", "b"]) == ""
