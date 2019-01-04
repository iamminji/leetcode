#### 문제 풀이

[Univalued Binary Tree](https://leetcode.com/problems/univalued-binary-tree/)


난이도는 Easy 이다.

트리 중에서 노드의 값이 다 같으면 true, 다르면 false 를 리턴하면 된다.

루트와 루트의 왼쪽, 루트와 루트의 오른쪽을 비교했고 재귀로 구현했다.

~~1번 트라이 했다. 정답률이 70퍼센트가 넘었던 문제여서..~~

다시 생각해보니까, 답이 틀린 것 같았다. 리턴 할 때 단순히 좌우의 boolean 비교를 했었는데 이럴 경우 서로 다른 부모 노드에서 각각 false 가 된다면 `false == false` 이므로 정답이 틀리게 되는 것이다.

그래서 testcase 하나 추가 해서 contribute 하고 재 제출 했다.
