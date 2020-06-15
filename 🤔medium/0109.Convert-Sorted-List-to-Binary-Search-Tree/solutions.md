## 문제 설명
이 문제는 [이 108번 문제](🙂easy/0108.Convert-Sorted-Array-to-Binary-Search-Tree) 과 굉장히 유사한 문제다.
다만 다른 점이 있다면 [108번 문제](🙂easy/0108.Convert-Sorted-Array-to-Binary-Search-Tree) 는 주어진 값이 정렬된 배열이고 109 번 문제는 정렬된 리스트라는 점이다.

쉽게 생각하자면 정렬된 리스트를 전부 순회해서 배열로 만들고 이전에 풀었던 108번 문제 처럼 풀 수도 있다.


## 풀이
### 리스트를 배열로 변경하여 풀이

```python3
class Solution:

    def recursive(self, start, end, nums):
        if start > end:
            return None
        mid = (start + end) // 2

        tree = TreeNode(nums[mid])
        tree.left = self.recursive(start, mid - 1, nums)
        tree.right = self.recursive(mid + 1, end, nums)
        return tree

    def sortedListToBST(self, head: ListNode) -> TreeNode:

        if head is None:
            return None

        nums = []
        while head is not None:
            nums.append(head.val)
            head = head.next

        mid = len(nums) // 2

        tree = TreeNode(nums[mid])
        tree.left = self.recursive(0, mid - 1, nums)
        tree.right = self.recursive(mid + 1, len(nums) - 1, nums)
        return tree
```
