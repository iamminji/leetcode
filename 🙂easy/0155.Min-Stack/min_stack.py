# 155. Min Stack
# https://leetcode.com/problems/min-stack/


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.arr = []

    def push(self, x: int) -> None:

        if len(self.arr) == 0:
            self.arr.append((x, x))
        else:
            self.arr.append((x, min(self.getMin(), x)))

    def pop(self) -> None:

        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1][0]

    def getMin(self) -> int:

        if len(self.arr) == 1:
            return self.arr[0][1]

        return self.arr[-1][1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
