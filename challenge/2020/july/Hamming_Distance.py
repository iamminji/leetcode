class Solution:
    def hammingDistanceUseString(self, x: int, y: int) -> int:
        p = bin(x)
        q = bin(y)

        res = 0
        for a, b in zip(("%031d" % int(p[2:])), ("%031d" % int(q[2:]))):
            if a != b:
                res += 1
        return res

    def hammingDistanceUseXor(self, x: int, y: int) -> int:
        p = x ^ y
        res = 0
        for q in bin(p)[2:]:
            if q == "1":
                res += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.hammingDistanceUseString(1, 4))
    print(sol.hammingDistanceUseXor(1, 4))
