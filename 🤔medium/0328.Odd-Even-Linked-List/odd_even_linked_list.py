# 328. Odd Even Linked List
# https://leetcode.com/problems/odd-even-linked-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 리스트 노드에서 홀수번째 리스트 노드가 먼저 나오고 남은 짝수 번째 리스트 노드가 나오게끔 만드는 문제다.
    # 주어진 조건 공간 복잡도 O(1), 시간 복잡도 O(nodes) 를 만족시켜야 한다.
    def oddEvenList(self, head: ListNode) -> ListNode:

        if head is None:
            return head

        # 짝수번째 노드만을 위한 더미 리스트 노드를 생성한다.
        dummy = ListNode(0)
        dummy_head = dummy
        temp = head

        while temp is not None and temp.next is not None:
            # 짝수번째 노드 만 이어 붙인다.
            dummy.next = temp.next
            dummy = dummy.next
            # 다음에 붙일 홀수번째 노드가 없으면 종료
            if temp.next.next is None:
                break
            temp.next = temp.next.next
            temp = temp.next

        # 짝수번째 노드의 마지막에 None 으로 업데이트
        # None 으로 안 바꾸면 기존 리스트 노드의 맨 마지막 홀수 번째 노드 부터 시작되어 리스트 노드가 cycle 을 가짐
        dummy.next = None
        # 홀수번째 노드의 맨 끝에 짝수번째 리스트 노드를 붙인다.
        temp.next = dummy_head.next
        return head


if __name__ == '__main__':
    sol = Solution()
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)
    print(sol.oddEvenList(node))
