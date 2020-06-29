# 706. Design HashMap
# https://leetcode.com/problems/design-hashmap/


class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
        return "Node(key:%s, value:%s, next:%s)" % (self.key, self.value, self.next)


class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 10000
        self.buckets = [Node() for _ in range(self.size)]

    def find_node(self, key: int):
        index = key % self.size
        prev = self.buckets[index]
        current = prev.next

        while current is not None:
            if current.key == key:
                return prev
            prev = prev.next
            current = current.next

        return prev

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        prev = self.find_node(key)
        if prev.next is None:
            prev.next = Node(key, value)
        else:
            # update
            prev.next.value = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        prev = self.find_node(key)
        if prev.next is None:
            return -1
        return prev.next.value

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        prev = self.find_node(key)
        if prev.next is not None:
            prev.next = prev.next.next


if __name__ == '__main__':
    # Your MyHashMap object will be instantiated and called as such:
    hashMap = MyHashMap()
    hashMap.put(1, 1)
    hashMap.put(2, 2)
    print(hashMap.put(92, 82))
    print(hashMap.put(12, 12))
    print(hashMap.get(12))
    print(hashMap.get(92))
    print(hashMap.put(102, 102))
    print(hashMap.put(202, 202))
    print(hashMap.put(12, 32))
    print(hashMap.get(12))
    print(hashMap.get(102))
