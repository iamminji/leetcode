# 67. Add Binary
# https://leetcode.com/problems/add-binary/


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # int 함수의 두 번째 인자 값을 활용하면 된다. 본문 처럼 2를 넣어주면 들어오는 string 값이 2진수라는 의미다.
        # bin 함수는 integer 를 바이너리로 변경 시켜주는데, 이 때 앞에 바이너리임을 표기해주기 위해 '0b' 가 붙는다.
        # 그러므로 결과엔 해당 글자를 제외해주기 위해서 2번째 부터 문자열이 시작됨을 의미하게 적어주면 된다.
        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == '__main__':
    sol = Solution()
    assert sol.addBinary("11", "1") == "100"
    assert sol.addBinary("1010", "1011") == "10101"
