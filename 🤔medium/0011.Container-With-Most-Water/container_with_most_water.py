# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/


class Solution:

    # height 가 있는 integer array 가 주어질 때 가장 넓은 넓이(문제에선 물이 담길수 있는 공간을 의미한다.) 를 찾는 문제다.
    # height 의 각 인덱스의 차이는 width 가 된다.

    def maxAreaTLE(self, height: 'List[int]') -> 'int':
        # TLE
        # 전체 루프를 돌아 계산하는 방법 O(n^2)
        res = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                res = max(res, (j - i) * min(height[i], height[j]))

        return res

    def maxArea(self, height: 'List[int]') -> 'int':

        # AC
        # O(n)

        i = 0
        j = len(height) - 1
        res = 0

        # 양 쪽 height 부터 시작하여 height 가 작은 쪽의 인덱스를 증가/감소 시켜가며 넓이 값을 최댓값으로 갱신해준다.
        while i < j:
            # 넓이 구하기
            res = max(res, (j - i) * min(height[i], height[j]))
            if height[j] < height[i]:
                j -= 1
            else:
                i += 1
        return res


if __name__ == '__main__':
    sol = Solution()
    assert sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
