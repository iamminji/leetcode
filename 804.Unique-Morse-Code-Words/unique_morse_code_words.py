# 804. Unique Morse Code Words
# https://leetcode.com/problems/unique-morse-code-words/description/


class Solution(object):
    """ Python2.7 """
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                 "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        res = set()
        for word in words:
            temp = []
            for w in word:
                index = ord(w) - 97
                temp.append(morse[index])
            res.add("".join(temp))
        return len(res)


if __name__ == "__main__":
    sol = Solution()
    print(sol.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
