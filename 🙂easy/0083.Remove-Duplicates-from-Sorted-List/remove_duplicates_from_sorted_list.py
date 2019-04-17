# 83. Remove Duplicates from Sorted List
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 리스트에서 중복된 노드를 제거한 링크드리스트를 리턴하는 문제다.
    def deleteDuplicates(self, head: ListNode) -> ListNode:

        # head 를 리턴할 것이므로 순회할 dummy로 copy 한다.
        dummy = head

        while dummy is not None and dummy.next is not None:
            # 값이 동일 할 때 다음 노드를 그 다다음 노드로 바꿔치기 한다.
            if dummy.val == dummy.next.val:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next

        return head
