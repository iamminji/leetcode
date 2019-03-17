# 394. Decode String
# https://leetcode.com/problems/decode-string/


class Solution:

    # 괄호 안의 글자를 바로 괄호 밖에 있는 숫자 만큼 반복하여 문자열을 만드는 문제다.
    def decodeString(self, s: str) -> str:

        nstack = list()
        cstack = list()
        i = 0
        cn, cc = 0, ""

        # 괄호 밖에 있는 숫자만큼 안의 글자를 반복해야 한다.
        # 하나는 숫자만, 하나는 문자열을 넣는 스택 두개를 만든다.

        # 숫자는 계속 누적한다. (10의 자리 이상이 들어올 경우 때문에)
        # 숫자가 끝나는 시점은 괄호를 만날 때이다. 그래서 괄호를 만나면 누적한 숫자를 스택에 넣는다.
        # 이 때 누적한 글자도 같이 넣어준다. (괄호 안의 문자 역시 2글자 이상 올 수 있으므로 누적하여 만든다.)
        # 괄호가 끝나면 누적했던 숫자와 글자를 pop 한다.

        # 그러면 스택에 있던 숫자만큼 기존 문자열을 반복 시키고 그 앞에 스택에서 pop한 문자를 더한다.

        # 그 이유는 3[a2[b]] 같은 경우의 예제를 보면 된다.
        # 가장 안의 문자열을 디코딩 하면 "bb" 가 되는데 이 "bb" 가 코드상에선 2 * "b" 인 것이고 기존에 넣었던 "a" 를 앞에 더해서 "abb" 를 만든다.
        # 이게 cc = c + n * cc 다.
        # c 는 이미 앞에서 넣어주었던 "a" 가 되고 cc 는 괄호를 만나기 바로 직전에 누적했던 문자열("bb")이다. 문자열이 나오려면 이미 문자열을 반복해야 하는 수가 스택에 들어가있다.
        # 룰을 보자면 그렇다.
        # 그래서 누적했던 문자열에 스택에서 pop 했던 수 만큼 곱해주고, 같이 반복해야 할 문자가 스택에 있으면 (빈 문자열이든) 앞에 더해주는 것이다.

        while i < len(s):
            if s[i] == "[":
                nstack.append(cn)
                cstack.append(cc)
                cn, cc = 0, ""
            elif s[i] == "]":
                n = nstack.pop()
                c = cstack.pop()
                cc = c + n * cc
            elif s[i].isdigit():
                cn = 10 * cn + int(s[i])
            else:
                cc = cc + s[i]
            i += 1

        return cc


if __name__ == '__main__':
    sol = Solution()
    assert sol.decodeString("3[a]2[bc]") == "aaabcbc"
    assert sol.decodeString("3[a2[c]]") == "accaccacc"
    assert sol.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"
