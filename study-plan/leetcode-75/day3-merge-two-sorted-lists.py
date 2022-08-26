# https://leetcode.com/problems/merge-two-sorted-lists/
# 21. Merge Two Sorted Lists

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # ListNode 생성 하여 풀이 (AC)

        if list1 is not None and list2 is None:
            return list1

        if list1 is None and list2 is not None:
            return list2

        if list1 is None and list2 is None:
            return None

        start = dummy = ListNode()

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                start.next = list1
                list1 = list1.next
            elif list1.val == list2.val:
                start.next = list1
                list1 = list1.next
            else:
                start.next = list2
                list2 = list2.next
            start = start.next

        if list1 is not None and list2 is None:
            start.next = list1

        if list2 is not None and list1 is None:
            start.next = list2

        return dummy.next

    def mergeTwoLists_2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # ListNode 생성 없이 풀이 (Discuss 참고)
        # 작은 값을 가진 리스트 노드를 이동 시켜서 연결 시키면 됨

        # list1이 None 이면 list2 가 list1의 가장 큰 값 보다 크다는 의미이므로
        # list2 를 리턴시킨다.
        if list1 is None:
            return list2

        if list2 is None:
            return list1

        if list1.val < list2.val:
            # list1을 이동시킴
            # 그리고 결과로 나온 값 (최소 l1 보다 큰 값) 을 l1 에 이어 붙인다.
            list1.next = self.mergeTwoLists_2(list1.next, list2)
            return list1
        else:
            # list2 이동
            # 같으면 사실 list1 이든 list2 든 누가 이동해도 상관 없음 (어느쪽에 붙여든 상관 없음)
            list2.next = self.mergeTwoLists_2(list1, list2.next)
            return list2
