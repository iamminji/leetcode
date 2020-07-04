class Solution:

    def nthUglyNumber(self, n: int) -> int:

        p2, p3, p5 = 0, 0, 0

        nums = [1 for _ in range(n)]
        for i in range(1, n):
            nums[i] = min(nums[p2] * 2, nums[p3] * 3, nums[p5] * 5)
            if nums[i] == nums[p2] * 2:
                p2 += 1
            if nums[i] == nums[p3] * 3:
                p3 += 1
            if nums[i] == nums[p5] * 5:
                p5 += 1

        return nums[-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.nthUglyNumber(10))
    print(sol.nthUglyNumber(21))
    print(sol.nthUglyNumber(1690))
