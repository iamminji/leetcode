#### 문제 풀이

[Convert BST to Greater Tree](https://leetcode.com/problems/convert-bst-to-greater-tree/description/) 라는 문제다
난이도는 **Easy** 이다.


Binary Tree가 주어지는데, 자기 값 보다 큰 값들만 더 해서 새로운 트리를 만드는 문제다.
BST(Binary Search Tree) 라고 주어졌기 때문에, 현재 값 보다 오른쪽 노드의 값은 항상 크고 왼쪽 노드는 항상 작다는 것을 알고 있다.

그렇기 때문에 재귀로 순회하면서 우측 값은 더 해주고 좌 측 값은 (현재 노드 값에) 더 해주지 않고 순회한다.