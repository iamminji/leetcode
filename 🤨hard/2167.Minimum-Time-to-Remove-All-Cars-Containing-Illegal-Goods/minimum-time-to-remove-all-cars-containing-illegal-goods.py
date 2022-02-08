# 2167. Minimum Time to Remove All Cars Containing Illegal Goods
# https://leetcode.com/problems/minimum-time-to-remove-all-cars-containing-illegal-goods/


# 53 maximum subarray 를 참고하면 된다.
class Solution:
    def minimumTime(self, s: str) -> int:

        size = len(s)
        res = size
        cost = 0

        for i in range(len(s)):
            if s[i] == "1":
                # 값이 1일 때
                # 1) 양 사이드에서 값을 제거하면 +1 이고
                # 2) 가운데 값을 빼면 +2 가 된다.
                # 그래서 현재 값 + 2 와 사이드에서(부터) 제거했을 때 값 i + 1 을 비교한다.
                cost = min(cost + 2, i + 1)
            # size - i - 1 을 하는 이유는 순회를 left -> right 로 하기 때문에
            # 가장 맨 오른쪽 값이 1이었어도 (사이드가 1이어도) 왼쪽에서 부터 계산해서 + 2 로 계산 된다.
            # 그래서 우측 부터 뺐을 때의 경우를 생각 해서 size - i - 1 을 하는 것이다.
            res = min(res, cost + size - i - 1)

        # 설명이 어려운데 kadne 알고리즘이라고
        # 53. maximum subarray 를 참고하도록 하자
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.minimumTime("1100101"))
    print(sol.minimumTime("0011111"))
