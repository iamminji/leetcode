class Solution:
    def countEven(self, num: int) -> int:
        res = 0
        for n in range(1, num + 1):
            ls = list(str(n))
            if sum([int(_) for _ in ls]) % 2 == 0:
                res += 1

        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.countEven(30))
    print(solution.countEven(4))
    print(solution.countEven(3))
