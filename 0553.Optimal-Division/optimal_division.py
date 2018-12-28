# 553. Optimal Division
# https://leetcode.com/problems/optimal-division/#/description


class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if len(nums) <= 2:
            return "/".join([str(_) for _ in nums])
        new_nums = "/".join([str(_) for _ in nums]).split("/")
        return new_nums[0] + "/(" + "/".join(new_nums[1:]) + ")"


if __name__ == "__main__":
    sol = Solution()
    print(sol.optimalDivision([1]))
    print(sol.optimalDivision([2, 3]))
    print(sol.optimalDivision([1000, 100, 10, 2]))
    print(sol.optimalDivision([1200, 500, 30, 10, 2]))
