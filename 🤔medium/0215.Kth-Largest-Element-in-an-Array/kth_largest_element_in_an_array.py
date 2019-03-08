# 215. Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/

from heapq import heappush, heappop


# 주어진 nums 배열에서 k 번째 큰 수를 찾는 문제

class Solution:

    def useSort(self, nums, k):
        # 주어진 배열을 정렬해서 k 번째 큰 수를 리턴한다.
        # AC 뜨고, O(nlogn) 이다.
        return sorted(nums)[len(nums) - k]

    def useHeap(self, nums, k):

        # heap 을 이용해서 k개 만큼만 nums 를 가지고 있는다.
        # heappush 하므로 결국엔 O(nlogn) 이다.
        h = []
        for n in nums:
            heappush(h, n)
            if len(h) > k:
                heappop(h)
        return h[0]

    def findKthLargest(self, nums: 'List[int]', k: 'int') -> 'int':
        return self.useHeap(nums, k)


if __name__ == '__main__':
    sol = Solution()
    assert sol.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert sol.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
