# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    # 문자열에서 가장 긴 중복(된 캐릭터가) 없는 부분 문자열을 찾는 문제다.

    def lengthOfLongestSubstring(self, s: str) -> int:
        # O(n^2) 으로 모든 문자들을 확인하며 최대 길이를 갱신해 준다.
        # 그냥 하면 TLE 가 뜨기 때문에, 현재 문자열에 중복된 문자가 있는지 확인하는 것을 하나 더 넣어주었다.
        # 이렇게 해도 AC가 뜬다.
        """
        res = 0
        for i in range(len(s)):
            d = set()
            for j in range(i + 1, len(s)+1):
                if s[j-1] in d:
                    break
                d.add(s[j-1])
                res = max(res, j - i)

        return res
        """

        # 여기서 전체 문자열을 계속 반복해서 보는게 아니라 봤던 문자열은 스킵 하도록 아래 처럼 변경하였다.
        if len(s) <= 1:
            return len(s)

        res = 0
        i, j = 0, 1
        d = set()

        while i < len(s) and j < len(s) + 1:
            if s[j] not in d:
                d.add(s[j])
                res = max(res, j - i)
                j += 1
            else:
                d.remove(s[i])
                i += 1
        return res
