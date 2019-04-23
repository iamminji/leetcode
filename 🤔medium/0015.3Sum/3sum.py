# 3Sum
# https://leetcode.com/problems/3sum/

from typing import List


class Solution:
    # 리스트에서 수 3개를 합하여 0이 되는 경우의 모든 값의 리스트를 리턴한다.
    # 단 중복된 조합은 제외한다.

    def threeSumTLE(self, nums: List[int]) -> List[List[int]]:

        # Time complexity O(n^3)
        # TLE
        res = []
        cache = set()
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    r = [nums[i], nums[j], nums[k]]
                    if tuple(sorted(r)) in cache:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.append(r)
                        cache.add(tuple(sorted(r)))
        return res

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Time complexity O(n^2)
        # 값을 정렬한 후에 좌/우의 값을 더해주면서 진행한다.
        # 더한 값이 음수면 필요로 하는 값은 양수이기 때문에 (0이 되어야 하므로) 왼쪽 인덱스를 오른쪽으로 증가시킨다. (정렬이 되어있으므로 큰 수로 증가시키는 것임)
        # 마찬가지로 더한 값이 양수면 필요로 하는 값은 음수이기 때문에 우측 인덱스를 좌측으로 감소시킨다.
        # 그리고 중복 조합을 제거하기 위해 set 을 쓴다.

        res = []
        snums = sorted(nums)
        cache = set()
        for i in range(len(snums)):

            left, right = i + 1, len(snums) - 1

            while left < right:

                if (snums[i], snums[left], snums[right]) in cache:
                    left += 1
                    right -= 1
                    continue

                s = snums[i] + snums[left] + snums[right]
                if s == 0:
                    res.append([snums[i], snums[left], snums[right]])
                    cache.add((snums[i], snums[left], snums[right]))
                    left += 1
                    right -= 1

                elif s < 0:
                    left += 1
                else:
                    right -= 1

        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.threeSum([-3, -1, 0, -1, 1, -4, 2, 3, 3, -6, -3, -3, 6, 2, 4]))
    print(sol.threeSum([2, 1, 4, 2, -4, 5, 3, -5, 1, 4, 0, 0, 3, 5, -6, 4, 4, 2, -3, -3, 6]))
