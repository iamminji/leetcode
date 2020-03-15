# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# 17. Letter Combinations of a Phone Number

from typing import List


class Solution:

    def recursive(self, i, sample, res):

        result = []

        if i == len(sample) - 1:
            for p in res:
                for q in sample[i]:
                    result.append(p + q)
            return result

        if i >= len(sample):
            return res

        for p in res:
            for q in sample[i]:
                for r in sample[i + 1]:
                    result.append(p + q + r)
        return self.recursive(i + 2, sample, result)

    def letterCombinations(self, digits: str) -> List[str]:
        m = {"2": ["a", "b", "c"],

             "3": ["d", "e", "f"],
             "4": ["g", "h", "i"],
             "5": ["j", "k", "l"],
             "6": ["m", "n", "o"],
             "7": ["p", "q", "r", "s"],
             "8": ["t", "u", "v"],
             "9": ["w", "x", "y", "z"]
             }

        if not digits:
            return []

        sample = []
        for d in digits:
            sample.append(m[d])

        return self.recursive(1, sample, sample[0])
