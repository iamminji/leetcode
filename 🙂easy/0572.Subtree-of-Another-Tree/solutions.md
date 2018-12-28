#### 문제 풀이

[572. Subtree of Another Tree](https://leetcode.com/problems/subtree-of-another-tree/description/) 
라는 문제다.


처음에 노드의 값이 유일하다고 생각해서 아래 처럼 했다.
좌측 값과 우측 값을 비교하는데, 시작하는 지점의 값이 다르면 while 문을 통해서 s의 좌/우측 값을 빼주고 비교하는 형식이었다.

<pre><code>
class Solution:

    def check(self, s_node, t_node):

        if s_node is None and t_node is None:
            return True

        if s_node is None:
            return False

        if t_node is None:
            return False

        return s_node.val == t_node.val \
               and self.check(s_node.left, t_node.left) \
               and self.check(s_node.right, t_node.right)

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        if s.val == t.val:
            return self.check(s.left, t.left) and self.check(s.right, t.right)

        s_queue = list()
        s_queue.append(s)
        while len(s_queue) > 0:
            s_node = s_queue.pop(0)

            if s_node is None:
                continue

            if s_node.val == t.val:
                return self.check(s_node.left, t.left) and self.check(s_node.right, t.right)

            s_queue.append(s_node.left)
            s_queue.append(s_node.right)
        return False
</code></pre>

그런데 중복 된 값이 들어왔다.
문제에 값의 중복에 대한 설명이 없었기 때문에 당연한 것이었다 😰

<code>[1,1] 과 [1]</code> 에 대한 예외였다.
t 가 끝났는데 s 의 값이 남아 있으면 False 라고 생각했지만, 
이와 같은 예에서는 s에서 1의 자식 노드가 1이고 그 1이 t와 같으므로
더 이상의 노드가 없어서 True 이다.


그래서 처음에 val을 비교하는 것도 빼고, while 루프에서 비교하는 것도 뺐다.
그 다음 s의 좌측과 s의 우측을 isSubtree로 다시 순회하게 했다.

마지막으로 좌 혹은 우 에서 True 가 나오면 True 로 리턴하게 했다.

<pre><code>
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """

        if self.check(s, t):
            return True

        if s is not None:
            return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        return False
</code></pre>


이러면 s의 길이 m, t의 길이를 n 으로 보면 시간 복잡도는
O(m * n) 이 된다.

s랑 t의 노드를 서로 비교하면서 순회하기 때문이다.
