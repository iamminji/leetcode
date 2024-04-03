# https://leetcode.com/problems/word-search/?envType=daily-question&envId=2024-04-03


from typing import List


class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.check(word, 0, i, j, board):
                    return True

        return False

    def check(self, word, k, i, j, board):

        if i < 0 or i >= len(board):
            return False

        if j < 0 or j >= len(board[0]):
            return False

        if k >= len(word):
            return False

        if word[k] != board[i][j]:
            return False

        # 여기 왔다는 건 단어를 다 찾았다는 의미이다.
        if k == len(word) - 1:
            return True

        # 이미 확인한 보드를 체크하는 부분
        board[i][j] = '#'

        # 끝까지 하나라도 갔으면 성공한 것이다.
        res = (
                self.check(word, k + 1, i + 1, j, board) or
                self.check(word, k + 1, i, j + 1, board) or
                self.check(word, k + 1, i - 1, j, board) or
                self.check(word, k + 1, i, j - 1, board)
        )
        # backtracing을 대비에 원복함
        board[i][j] = word[k]

        return res


if __name__ == '__main__':
    solution = Solution()

    print(solution.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
    print(solution.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"))
    print(solution.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"))
    print(solution.exist([["a", "b"], ["c", "d"]], "bacd"))
