# 238. Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/description/


class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        res = 1
        for num in nums:
            res *= num

        if res == 0:
            return nums

        for i in range(len(nums)):
            nums[i] = res // nums[i]

        print(nums)
        return nums


if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf([0, 0]))
