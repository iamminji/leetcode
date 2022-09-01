from typing import List


class Solution:

    def dfs(self, i, j, board, index, words):

        if i >= len(board) or j >= len(board[i]) or i < 0 or j < 0:
            return False

        if index >= len(words):
            return False

        if board[i][j] != words[index]:
            return False

        if index == len(words) - 1:
            return True

        board[i][j] = "#"
        res = self.dfs(i - 1, j, board, index + 1, words) or \
              self.dfs(i + 1, j, board, index + 1, words) or \
              self.dfs(i, j + 1, board, index + 1, words) or \
              self.dfs(i, j - 1, board, index + 1, words)
        board[i][j] = words[index]
        return res

    def exist(self, board: List[List[str]], word: str) -> bool:
        words = list(word)
        for i in range(len(board)):
            for j in range(len(board[i])):
                if words[0] == board[i][j]:
                    result = self.dfs(i, j, board, 0, words)
                    if result:
                        return True

        return False


if __name__ == '__main__':
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]

    sol = Solution()
    print(sol.exist(board, "ABCCED"))
    print(sol.exist(board, "SEE"))
    print(sol.exist(board, "ABCB"))

    board2 = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
    print(sol.exist(board2, "AAB"))

    board3 = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
    print(sol.exist(board3, "ABCESEEEFS"))
