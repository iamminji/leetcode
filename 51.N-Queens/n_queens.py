# 51. N-Queens
# https://leetcode.com/problems/n-queens/description/


class Solution:

    def __init__(self):
        self.result = list()

    def is_safe(self, board, col, row):
        for r in range(0, row):
            if board[col][r] == 'Q':
                return False

        c, r = col, row
        while c >= 0 and r >= 0:
            if board[c][r] == 'Q':
                return False
            c -= 1
            r -= 1

        c, r = col, row
        while r >= 0 and c < len(board):
            if board[c][r] == 'Q':
                return False
            c += 1
            r -= 1

        return True

    def dfs(self, board, row):

        if row >= len(board):
            res = ["".join(board[_]) for _ in range(len(board[0]))]
            self.result.append(res)
            return

        for col in range(0, len(board)):
            if self.is_safe(board, col, row):
                board[col][row] = 'Q'
                self.dfs(board, row + 1)
                board[col][row] = '.'
        return

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        board = [['.' for _ in range(n)] for _ in range(n)]
        self.dfs(board, 0)
        return self.result


if __name__ == "__main__":
    sol = Solution()
    print(sol.solveNQueens(4))
    print(sol.solveNQueens(8))
