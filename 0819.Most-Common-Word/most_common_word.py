# 819. Most Common Word
# https://leetcode.com/problems/most-common-word/description/

from collections import defaultdict
from string import punctuation


class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        word = defaultdict(int)
        banned = set(banned)
        for w in paragraph.split(' '):
            for p in punctuation:
                w = w.replace(p, '')
            w = w.lower()
            if w not in banned:
                word[w] += 1

        return sorted(word, key=lambda x: word[x], reverse=True)[0]


if __name__ == "__main__":
    sol = Solution()
    print(sol.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit."
                             , ["hit"]))
