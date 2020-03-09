# https://leetcode.com/problems/group-anagrams/
# 49. Group Anagrams

from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = []
        d = defaultdict(list)
        for s in strs:
            word = "".join(sorted(s))
            d[word].append(s)

        for k, v in d.items():
            result.append(v)
        return result
