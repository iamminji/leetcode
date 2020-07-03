## 문제
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

```
For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
```

### 솔루션
알고리즘 보다는 구현 문제였다. 

#### 해결
tree 순회하면서 리스트에 값을 넣는데, 이 때 depth 를 리스트의 인덱스로 잡고 넣어주면 된다.
리턴할 때는 리스트의 역순으로 리턴하면 정답이 나온다.

```python3
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:

        if root is None:
            return []

        queue = deque()
        queue.append([root, 0])

        result = []

        while queue:
            node, depth = queue.popleft()

            if len(result) <= depth:
                result.append([node.val])
            else:
                result[depth].append(node.val)

            if node.left is not None:
                queue.append([node.left, depth+1])

            if node.right is not None:
                queue.append([node.right, depth+1])

        return result[::-1]
```
