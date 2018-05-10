# 821. Shortest Distance to a Character
# https://leetcode.com/problems/shortest-distance-to-a-character/description/


class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """

        pos = []
        for i, s in enumerate(S):
            if s == C:
                pos.append(i)

        j = -1
        result = []
        for i, s in enumerate(S):
            if s == C:
                result.append(0)
                j += 1
            else:
                if j < len(pos) - 1:
                    result.append(min(abs(i-pos[j]), abs(pos[j+1] - i)))
                else:
                    result.append(min(abs(i - pos[j]), abs(pos[j] - i)))

        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestToChar("abaaa", "b"))
    print(sol.shortestToChar("abba", "b"))
    print(sol.shortestToChar("loveleetcode", "e"))