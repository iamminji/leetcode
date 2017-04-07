from collections import deque


def my_compare(a, b):
    if int(str(a) + str(b)) > int(str(a) + str(b)):
        return 1
    elif int(str(a) + str(b)) < int(str(a) + str(b)):
        return -1
    else:
        return 0


class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        result = list()
        for i in range(0, len(nums)):
            for j in range(i, len(nums)):
                if int(str(nums[i])+str(nums[j])) > int(str(nums[j])+str(nums[i])):
                    nums[i], nums[j] = nums[j], nums[i]

        for num in nums:
            result.append(str(num))

        return str(int("".join(result[::-1])))



if __name__ == "__main__":
    sol = Solution()
    # print(sol.largestNumber([1, 2, 30]))
    print(sol.largestNumber([1, 2, 30]))
    print(sol.largestNumber([93, 51, 65, 84, 91, 78, 99, 71, 97, 9]))
