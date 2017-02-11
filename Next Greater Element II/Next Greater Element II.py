# https://leetcode.com/problems/next-greater-element-ii/
# Time Limit Exceeded


class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = list()
        cur_idx = 0
        idx = 0
        while cur_idx < len(nums):
            idx += 1
            if nums[cur_idx] < nums[idx % len(nums)]:
                result.append(nums[idx % len(nums)])
                cur_idx += 1
                idx = cur_idx
                continue
            if cur_idx == (idx % len(nums)):
                cur_idx += 1
                idx = cur_idx
                result.append(-1)

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.nextGreaterElements([100, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
