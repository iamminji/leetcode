# 532. K-diff Pairs in an Array
# https://leetcode.com/problems/k-diff-pairs-in-an-array/


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        new_nums = sorted(nums)
        idx = 0
        jdx = 1
        count = 0
        visited = dict()
        while jdx < len(nums):
            num_i, num_j = new_nums[idx], new_nums[jdx]
            if num_i + k == num_j:
                if (num_i, num_j) not in visited and \
                                (num_j, num_i) not in visited:
                    count += 1
                visited[(num_i, num_j)] = True
                visited[(num_j, num_i)] = True
            elif num_i + k > num_j:
                jdx += 1
                continue
            idx += 1
            jdx = idx + 1
        return count


if __name__ == '__main__':
    sol = Solution()
    print(sol.findPairs([1, 2, 3, 4, 5], 3))
    print(sol.findPairs([1, 2, 3, 101, 100], 99))
    print(sol.findPairs([1, 1, 1, 1, 2], 0))
    print(sol.findPairs([3, 1, 4, 1, 5], 2))
    print(sol.findPairs([1, 1, 1, 2, 2], 0))
    print(sol.findPairs([6, 7, 3, 6, 4, 6, 3, 5, 6, 9], 4))
