# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        stack = list()
        water = 0
        i = 0
        while i < len(height):
            if not stack or height[stack[-1]] > height[i]:
                stack.append(i)
                i += 1
            else:
                bottom = stack.pop()
                if len(stack) > 0:
                    water += (min(height[i], height[stack[-1]]) - height[bottom]) * (i - stack[-1] - 1)
        return water
