# https://leetcode.com/problems/assign-cookies/
# python 3.6

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        result = 0
        g.sort()
        s.sort()
        g_idx, s_idx = 0, 0
        while g_idx < len(g) and s_idx < len(s):
            if g[g_idx] <= s[s_idx]:
                result += 1
                g_idx += 1
                s_idx += 1
            else:
                s_idx += 1

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.findContentChildren([1, 2, 3], [1, 1]))
    print(sol.findContentChildren([10, 9, 8, 7], [5, 6, 7, 8]))
    print(sol.findContentChildren([10, 11, 12, 13], [1, 1, 2, 2, 15, 15, 15, 15]))
