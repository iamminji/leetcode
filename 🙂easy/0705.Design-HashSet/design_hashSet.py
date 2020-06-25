# 705. Design HashSet
# https://leetcode.com/problems/design-hashset/


class Node:
    def __init__(self, key=None):
        self.key = key
        self.next = None

    def __str__(self):
        return "Node(%s)" % self.key


class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.buckets = [Node() for _ in range(self.size)]

    def find_node(self, key) -> (bool, Node):
        """
        :param key:
        :return: key 에 해당하는 값을 찾았는지 여부, 추가해야할 Node 이전 노드
        """
        index = key % self.size
        prev = self.buckets[index]
        current = prev.next

        while current is not None:
            if current.key == key:
                return True, prev
            current = current.next
            prev = prev.next
        return False, prev

    def add(self, key: int) -> None:
        exist, prev = self.find_node(key)
        if not exist:
            prev.next = Node(key)
        return None

    def remove(self, key: int) -> None:
        exist, prev = self.find_node(key)
        if exist:
            prev.next = prev.next.next
        return None

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        exist, prev = self.find_node(key)
        return exist is True


if __name__ == '__main__':
    obj = MyHashSet()

    obj.add(1)
    obj.add(2)
    print(obj.contains(1))
    print(obj.contains(4))
