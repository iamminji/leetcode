# https://leetcode.com/problems/divisor-game/
# 1025. Divisor Game


class Solution:
    def divisorGame(self, N: int) -> bool:

        alice = True
        while N > 2:
            for n in range(1, N):
                if N % n == 0:
                    alice = not alice
                    N -= n
                    break
        return alice if N > 1 else False



