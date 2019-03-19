# 203. Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 링크드리스트가 주어질 때 val 에 해당하는 값을 삭제하는 문제다.
    def removeElements(self, head: ListNode, val: int) -> ListNode:

        node = head

        # 주어진 리스트 노드를 순회하면서 주어진 값 val 과 비교하여
        # 해당 val 이 등장하면 그 노드를 스킵하는 로직이다. (노드의 다음-다음 노드를 노드의 다음 노드로 연결)
        # node와 head를 따로 두는 이유는 순회하면서 이미 포인터 가 끝에 다다랐기 때문에 시작 포인터를 잡아주려고 그런 것이다. (주어진 구조체에 prev가 없어서)
        while node.next is not None:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next

        # node.next 부터 시작했으므로 시작 노드가 val 과 같은 경우가 있을 수 있다.
        # 관련하여 예외처리를 해 준다.
        return head if head.val != val else head.next


if __name__ == '__main__':
    test_cases = """
    Input:  1->2->6->3->4->5->6, val = 6
    Output: 1->2->3->4->5
    """
