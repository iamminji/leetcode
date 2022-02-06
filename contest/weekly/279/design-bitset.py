# https://leetcode.com/contest/weekly-contest-279/problems/design-bitset/
class Bitset:

    def __init__(self, size: int):
        self.nums = []
        self.fnums = []
        self.size = size
        self.one_count = 0

        for i in range(size):
            self.nums.append(0)
            self.fnums.append(1)

    def fix(self, idx: int) -> None:
        if self.nums[idx] == 0:
            self.one_count += 1

        self.nums[idx] = 1
        self.fnums[idx] = 0

    def unfix(self, idx: int) -> None:
        if self.nums[idx] == 1:
            self.one_count -= 1

        self.nums[idx] = 0
        self.fnums[idx] = 1

    def flip(self) -> None:
        self.fnums, self.nums = self.nums, self.fnums
        self.one_count = self.size - self.one_count

    def all(self) -> bool:
        return self.one_count == self.size

    def one(self) -> bool:
        return self.one_count > 0

    def count(self) -> int:
        return self.one_count

    def toString(self) -> str:
        return "".join([str(_) for _ in self.nums])
