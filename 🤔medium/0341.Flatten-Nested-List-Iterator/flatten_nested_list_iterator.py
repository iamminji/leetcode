# 341. Flatten Nested List Iterator
# https://leetcode.com/problems/flatten-nested-list-iterator/

from collections import deque


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """

    def getList(self) -> [NestedInteger]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """


class NestedIterator:

    def __init__(self, nestedList: [NestedInteger]):
        self.queue = deque()
        self.flatten(nestedList)

    def flatten(self, items):
        if isinstance(items, list):
            for item in items:
                if item.isInteger():
                    self.queue.append(item.getInteger())
                else:
                    self.flatten(item.getList())
        else:
            self.queue.append(items.getInteger())

    def next(self) -> int:
        return self.queue.popleft()

    def hasNext(self) -> bool:
        return len(self.queue) > 0
