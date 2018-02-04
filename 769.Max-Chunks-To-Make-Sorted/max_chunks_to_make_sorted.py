# 769. Max Chunks To Make Sorted
# https://leetcode.com/problems/max-chunks-to-make-sorted/description/


class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        chunk = 0
        m = 0

        for idx, num in enumerate(arr):
            m = max(m, num)
            if idx == m:
                chunk += 1

        return chunk


if __name__ == "__main__":
    sol = Solution()
    print(sol.maxChunksToSorted([4, 3, 1, 2, 0]))
