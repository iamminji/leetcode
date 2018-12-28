# 79. Word Search
# https://leetcode.com/problems/word-search/#/description


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        res = False
        for idx in range(0, len(board)):
            for jdx in range(0, len(board[0])):
                res = res or self.check_board(idx, jdx, board, 0, word)

        return res

    def check_board(self, i, j, board, k, word):

        if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0:
            return False

        if board[i][j] != word[k]:
            return False

        if k == len(word) - 1:
            return True

        board[i][j] = "#"
        res = self.check_board(i - 1, j, board, k + 1, word) or \
              self.check_board(i + 1, j, board, k + 1, word) or \
              self.check_board(i, j + 1, board, k + 1, word) or \
              self.check_board(i, j - 1, board, k + 1, word)
        board[i][j] = word[k]
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.exist([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], "ABCCED"))
