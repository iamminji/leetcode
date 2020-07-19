class Solution:
    def addBinary(self, a: 'str', b: 'str') -> 'str':

        if len(a) == 0 and len(b) != 0:
            return b
        if len(b) == 0 and len(a) != 0:
            return a
        i, j = len(a) - 1, len(b) - 1
        r = "0"

        result = []

        while i >= 0 and j >= 0:
            p, q = a[i], b[j]
            if r == "1":
                if p == "1" and q == "1":
                    result.append("1")
                elif (p == "1" and q == "0") or (p == "0" and q == "1"):
                    result.append("0")
                else:
                    result.append("1")
                    r = "0"
            else:
                if p == "1" and q == "1":
                    result.append("0")
                    r = "1"
                elif p == "0" and q == "0":
                    result.append("0")
                else:
                    result.append("1")
            i -= 1
            j -= 1

        if len(a) > len(b):
            while i >= 0:
                if r == "1":
                    if a[i] == "1":
                        result.append("0")
                        r = "1"
                    else:
                        result.append("1")
                        r = "0"
                else:
                    result.append(a[i])
                i -= 1
        elif len(b) > len(a):
            while j >= 0:
                if r == "1":
                    if b[j] == "1":
                        result.append("0")
                        r = "1"
                    else:
                        result.append("1")
                        r = "0"
                else:
                    result.append(b[j])
                j -= 1

        if r == "1":
            result.append(r)

        return "".join(result[::-1])


if __name__ == '__main__':
    sol = Solution()
    a = "11"
    b = "1"
    print(sol.addBinary(a, b))
    a = "1010"
    b = "1011"
    print(sol.addBinary(a, b))
