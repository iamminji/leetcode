#### 문제 풀이

[543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/description/) 
라는 문제다.

난이도는 **Easy** 이다.


트리에서 가장 긴 길이(?)를 찾는 문젠데, 가장 긴 길이는 무조건 최 상위 부모 노드를 포함해야 하고
그 길이는 좌 트리의 가장 긴 길이 + 우 트리의 가장 긴 길이 일 거라고 생각했다.

그래서 재귀로 돌면서 max 값을 갱신해주면 되지 않을까..생각했고 아래처럼 해서 틀렸다.

<pre><code>
class Solution:

    def recursive(self, node, level):
        if node is None:
            return level

        return max(self.recursive(node.left, level + 1),
                   self.recursive(node.right, level + 1))


    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0
        return self.recursive(root.left, 0) + self.recursive(root.right, 0)
</code></pre>

틀린 예제는
<code>[4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]
</code>
이건데, 알고보니까 문제에서 가장 긴 길이는 루트 노드를 포함하지 않을 수도 있다고 한다..


그래서 total 값으로 클래스 인스턴스 변수를 하나 만들어서 max로 갱신하고
결과로 total과 비교해서 리턴했더니 통과 되었다.


