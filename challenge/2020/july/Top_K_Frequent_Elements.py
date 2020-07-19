from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        counter = sorted(counter.items(), key=lambda x: -x[1])
        result = []
        cnt = 0
        for item in counter:
            if cnt == k:
                break
            result.append(item[0])
            cnt += 1
        return result


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    sol = Solution()
    print(sol.topKFrequent(nums, k))
