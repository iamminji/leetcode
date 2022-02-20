from collections import Counter


# Solve the problem after Contest
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        alp = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]
        alp.reverse()
        counter = Counter(s)
        result = []

        i = 0
        goto = False
        while i < len(alp):
            if counter[alp[i]] == 0:
                del counter[alp[i]]
                i += 1
                continue

            if counter[alp[i]] > 0:
                if goto:
                    result.append(alp[i])
                    counter[alp[i]] -= 1
                    goto = False
                    i = 0
                    continue

                if counter[alp[i]] >= repeatLimit:
                    for _ in range(repeatLimit):
                        result.append(alp[i])
                    counter[alp[i]] -= repeatLimit
                    if counter[alp[i]] > 0:
                        goto = True
                elif counter[alp[i]] > 0:
                    for _ in range(counter[alp[i]]):
                        result.append(alp[i])
                    counter[alp[i]] = 0
                    goto = False
                i += 1
            else:
                i += 1
                goto = False

        for c in counter:
            if counter[c] > 0 and result[-1] != c:
                result.append(c)

        return "".join(result)


if __name__ == '__main__':
    solution = Solution()
    print(solution.repeatLimitedString("cczazcc", 3))
    print(solution.repeatLimitedString("aababab", 2))
    print(solution.repeatLimitedString("xyutfpopdynbadwtvmxiemmusevduloxwvpkjioizvanetecnuqbqqdtrwrkgt", 1))
