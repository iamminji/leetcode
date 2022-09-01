# 2020.07.11
#  Flatten a Multilevel Doubly Linked List

from heapq import heappop, heappush


# Definition for a Node.
class Node:
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Node') -> 'Node':

        if head is None:
            return None

        heap = []

        item = (0, head)
        heappush(heap, item)

        dummy = Node(0, None, None, None)
        result = dummy

        while heap:
            depth, node = heappop(heap)

            dummy.next = node
            node.prev = dummy

            if node.child is not None:
                heappush(heap, (depth - 1, node.child))
            if node.next is not None:
                heappush(heap, (depth, node.next))

            dummy = dummy.next
            dummy.next = None
            dummy.child = None

        ret = result.next
        ret.prev = None
        return ret


if __name__ == '__main__':
    node = Node(1)
    node2 = Node(2)

    node.next = node2
    node2.prev = node

    node.child = Node(3)

    sol = Solution()
    result = sol.flatten(node)

    while result is not None:
        print(result.val)
        result = result.next
