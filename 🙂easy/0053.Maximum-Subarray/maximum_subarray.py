# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/

from typing import List


class Solution:
    # 주어진 integer 리스트에서 가장 큰 부분 합(sum)을 구하는 문제다.
    # 여기서 가장 maximum sum 은 리스트에서 연속적인 부분 리스트의 합이 되어야 한다.
    def maxSubArray(self, nums: List[int]) -> int:
        temp, result = nums[0], nums[0]

        # 값 두개를 사용해서 풀 수 있다.
        # 첫번째 값 temp 는 현재 값과 현재 값을 포함한 sum 중 큰 값을 갖고 가고
        # 두번째 값 result 는 그러한 temp 중에 가장 큰 값을 가지고 간다.
        # 값 2개를 사용하는 이유는, 특히 temp 를 사용하는 이유는 구해야 하는 합은 부분 리스트의 합이면서
        # 해당 리스트엔 음수 값이 들어갈 수 있다. 그렇기 때문에 음수 값을 포함한 부분 리스트의 합이 커지는 구간이 생길 수 있으므로
        # 현재 값을 포함한 maximum 값을 확인해야 하는 것이다.
        for i in range(1, len(nums)):
            temp = max(temp + nums[i], nums[i])
            result = max(result, temp)

        return result
