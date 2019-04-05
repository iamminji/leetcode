# 942. DI String Match
# https://leetcode.com/problems/di-string-match/

from typing import List

class Solution:
    # 0 부터 len(S) 까지의 숫자가 있을 때,
    # 알파벳 D 인 경우는 감소를 I 인 경우에는 증가하는 숫자 리스트를 만드는 문제다.
    def diStringMatch(self, S: str) -> List[int]:
        end = len(S)
        start = 0

        # 제일 작은 수와 큰 수를 사전에 미리 정의하고
        # 알파벳이 등장할 때 해당하는 값을 증가/감소 시켜가며 넣어주면 된다.
        # 전체 수의 길이는 문자열 길이 + 1 이므로 마지막 글자만 한번 더 넣어준다. (결국 start와 end는 같게 된다.)
        res = []
        for s in S:
            if s == "I":
                res.append(start)
                start += 1
            else:
                res.append(end)
                end -= 1

        res.append(start)
        return res
