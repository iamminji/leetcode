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
        i, j = 0, 0
        d = set()

        # 포인터 두 개로 중복 없는 최대 문자열의 길이를 찾는다.
        # 예를 들어 0 번째 부터 5번째 문자열 안에 중복된 문자가 없으면 현재 res 값은 6이 된다.
        # 이 때 set 안에는 0번 부터 5번째 글자가 들어가 있게 된다.
        # 6번째 글자가 중복되었다면 중복이 안될 때 까지 i를 0에서 부터 증가시키면서 set 에서 제거해준다. (i를 j까지 당겨준다고 생각할 수 있다.)
        # window 를 옮겨준다고 생각하면 된다.

        # 이를 sliding window 라 부른다.
        while i < len(s) and j < len(s):
            if s[j] not in d:
                d.add(s[j])
                res = max(res, j - i + 1)
                j += 1
            else:
                d.remove(s[i])
                i += 1
        return res
