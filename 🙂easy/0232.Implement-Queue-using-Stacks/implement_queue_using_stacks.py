# 232. Implement Queue using Stacks
# https://leetcode.com/problems/implement-queue-using-stacks/


class MyQueue(object):

    def __init__(self):
        # stack 은 python list 로 쓴다.
        self.stack1 = []
        self.stack2 = []

    def push(self, item):
        self.stack1.append(item)

    def pop(self):
        if len(self.stack2) == 0:
            while self.stack1:
                data = self.stack1.pop()
                self.stack2.append(data)

        item = self.stack2.pop()
        return item

    def peek(self):
        if len(self.stack2) > 0:
            return self.stack2[-1]
        return self.stack1[0]

    def empty(self):
        return len(self.stack2) == 0 and len(self.stack1) == 0
