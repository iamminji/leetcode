# 655. Print Binary Tree
# https://leetcode.com/problems/print-binary-tree/description/


"""
     1
    / \
   2   3
    \
     4
     
self.res = {"0": "1", "0L": "2", "0R": "3", "0LR": "4"} 형태로 되어 있음
"0LR"은 "0L"의 오른쪽이고 이 때 인덱스를 jump_list에 미리 넣어두고 꺼내서 더해주거나("R") 빼줌("L")
"""


from collections import deque


class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """

        if root is not None:
            self.res = {"0": str(root.val)}
        else:
            return [[""]]

        if root.left is not None:
            self.check_node(root.left, "0" + "L")
        if root.right is not None:
            self.check_node(root.right, "0" + "R")

        depth = max([len(k) for k in self.res])
        width = int(pow(2, depth) - 1)

        jump_list = list()
        for d in range(depth - 2, -1, -1):
            jump_list.append(pow(2, d))

        key_set = deque(sorted(self.res, key=lambda item: (len(item), item)))

        inner = ["" for _ in range(width)]
        # 항상 첫번째 key는 root 라고 생각
        cur_key = key_set.popleft()
        idx = -1
        inner[width // 2] = self.res[cur_key]
        current_length = 1

        total_list = list()
        cur_idx_dict = dict()
        cur_idx_dict[cur_key] = width // 2

        while key_set:
            key = key_set.popleft()
            if current_length != len(key):
                total_list.append(inner)
                inner = ["" for _ in range(width)]
                idx += 1
                current_length = len(key)

            new_val = ""
            for ck in cur_idx_dict:
                if key == ck + "L":
                    inner[cur_idx_dict[ck] - jump_list[idx]] = self.res[key]
                    new_val = cur_idx_dict[ck] - jump_list[idx]
                elif key == ck + "R":
                    inner[cur_idx_dict[ck] + jump_list[idx]] = self.res[key]
                    new_val = cur_idx_dict[ck] + jump_list[idx]

            if new_val:
                cur_idx_dict[key] = new_val

        if inner:
            total_list.append(inner)
        return total_list

    def check_node(self, node, key):
        self.res[key] = str(node.val)

        if node.left is not None:
            self.check_node(node.left, key + "L")
        if node.right is not None:
            self.check_node(node.right, key + "R")
        return
