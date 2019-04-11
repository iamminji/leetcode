# 696. Count Binary Substrings
# https://leetcode.com/problems/count-binary-substrings/


class Solution:
    # 0과 1로 이루어진 문자열이 들어온다. 이 때 0과 1이 같은 카운트로 등장하는 모든 부분 문자열의 개수를 리턴하는 문제다.
    def countBinarySubstrings(self, s: str) -> int:

        # 들어오는 0과 1로 이루어진 문자열을 그룹핑한 카운트를 우선 구한다.
        # 예를 들면 "00110011" 은 [2, 2, 2, 2] 가 된다. 이를 group 이라고 우선 한다.
        # "00110011" 은 "0011", "01", "1100", "10", "01", "0011" 총 6개의 경우가 나온다.
        # 첫번째 "0011" 은 group[0]과 group[1] 의 결과 값이다.
        # 두번째 "01" 은 "0011" 의 부분 문자열이다.
        # 여기까지의 결과 값은 group[0] 과 group[1] 의 최소값 2와 같다.
        # 즉 min(group[i-1], group[i]) 을 누적하는 것이다.
        # 최소값으로 하는 이유는 "100" 이라는 [1, 2] 라는 리스트가 만들어진다면 여기서 생길 수 있는 부분 문자열은 "10" 이며 하나 밖에 없다.
        # 즉 같은 숫자로 그룹핑을 했는데 나올 수 있는 같은 문자열은 최소값일 수 밖에 없다는 건데
        # (1이 하나고 0이 두개인데 연속적이어야 한다면 최소 값을 따를 수 밖에 없겠지?) 뭔가 설명을 잘 못 풀어 쓰겠다.

        group = [1]
        pre = s[0]
        pre_idx = 0
        for i in range(1, len(s)):
            if pre == s[i]:
                group[pre_idx] += 1
            else:
                group.append(1)
                pre_idx += 1
                pre = s[i]

        res = 0
        for i in range(1, len(group)):
            res += min(group[i - 1], group[i])

        return res


if __name__ == '__main__':
    sol = Solution()
    assert sol.countBinarySubstrings("00110011") == 6
    assert sol.countBinarySubstrings("10101") == 4
    assert sol.countBinarySubstrings("1100") == 2
