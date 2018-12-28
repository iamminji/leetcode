# 495. Teemo Attacking
# https://leetcode.com/problems/teemo-attacking/description/


class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        result = 0
        cur_time = 0
        for ts in timeSeries:
            if ts >= cur_time:
                result += duration
            else:
                result += ts + duration - cur_time
            cur_time = ts + duration

        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.findPoisonedDuration([1, 2], 2))
    print(sol.findPoisonedDuration([1, 4], 2))
    print(sol.findPoisonedDuration([1, 5, 100], 2))
