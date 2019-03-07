# 894. All Possible Full Binary Trees
# https://leetcode.com/problems/all-possible-full-binary-trees/


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
        주어진 N개의 숫자만큼 노드를 가지고 있을 때 full binary tree node 를 생성하는 문제다.
        full binary tree node는 자식 노드가 없거나 자식 노드가 둘이다.

    """

    def allPossibleFBT(self, N):

        # 노드가 1개 일 때 생성
        if N == 1:
            return [TreeNode(0)]

        N -= 1

        ans = []

        # 부모 노드 1개를 제외한 자식 노드 2개씩 만들어주기 위해서 i는 1부터 N 까지 2 씩 증가한다.
        # i 는 생성 할 트리 노드 개수가 된다.
        # 좌측 노드가 i 개 생성되면 우측 노드는 N-i 개 생성되어야 한다.
        for i in range(1, N, 2):
            # 좌측 노드 생성
            left = self.allPossibleFBT(i)
            # 우측 노드 생성
            right = self.allPossibleFBT(N - i)
            for nl in left:
                for nr in right:
                    # 부모 노드
                    node = TreeNode(0)
                    # 좌측에서 나온 노드 리스트로 업데이트
                    node.left = nl
                    # 우측에서 나온 노드 리스트로 업데이트
                    node.right = nr
                    # 결과 값 저장
                    ans.append(node)
        return ans


if __name__ == '__main__':
    from common import pp

    sol = Solution()
    res = sol.allPossibleFBT(5)
    for r in res:
        print(pp.FullBinaryTreeNodePrettyPrinter.pp(r))
    # [[0, 0, 0, None, None, 0, 0, None, None, 0, 0], [0, 0, 0, None, None, 0, 0, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, None, None, None, None, 0, 0],
    #  [0, 0, 0, 0, 0, None, None, 0, 0]]
