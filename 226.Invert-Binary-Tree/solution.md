#### 문제 풀이

[Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/description/) 라는 문제다
난이도는 **Easy** 이다.

주어진 트리노드의 좌/우를 변경하는 문제이다.
큐에 현재 노드를 넣고, 큐가 빌 때 까지 노드를 하나씩 꺼내가면서 좌, 우를 swap 하면 된다.

시간 복잡도는 O(n)이고 공간 복잡도도 O(n)이다.