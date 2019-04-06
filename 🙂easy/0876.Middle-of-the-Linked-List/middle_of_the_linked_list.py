# 876. Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 리스트 노드에서 중간 노드를 찾아 그 노드 이후를 리턴하는 문제다.
    def middleNode(self, head: ListNode) -> ListNode:
        # 포인터 2개를 이용해서 풀 수 있다.
        # 리스트 노드가 2k 개 있다고 하였을 때 마지막에 하나의 노드는 2번씩 진행하고 나머지 하나는 한번씩 진행한다고 하면
        # 2번씩 진행하는 노드가 마지막에 다다를 때의 이터레이터 횟수는 k고 이는 다른 노드의 현재까지 진행한 횟수와 같다.
        # 그리고 이 k가 리스트 노드의 중간 값과도 같다.
        # 홀수개의 리스트 노드가 있을 때도 상관 없다. 문제에서 미들 노드가 두개면 두번째 이후를 리턴하라고 하였기 때문이다.

        # 사이클 디텍션할 때 사용하는 tortoise and hare 알고리즘을 같이 생각해보면 좋을 것 같다.

        node1 = head
        node2 = head
        while node1 is not None and node1.next is not None:
            node1 = node1.next.next
            node2 = node2.next

        return node2
