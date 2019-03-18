# 434. Number of Segments in a String
# https://leetcode.com/problems/number-of-segments-in-a-string/


class Solution:
    # 문장에서 단어(연속된 문자열) 을 찾는 문제다.
    # 빌트인 함수를 사용하면 금방 풀 수 있어서,
    # 언어에 대한 익숙함 확인 용 및 아이스브레이킹으로 나올 것만 같은 문제였다.
    def countSegments(self, s: str) -> int:
        return len(s.split())
