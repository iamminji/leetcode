# 84. Largest Rectangle in Histogram
# https://leetcode.com/problems/largest-rectangle-in-histogram/


class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        stack = list()
        max_area = 0
        i = 0
        while i < len(heights):
            if len(stack) == 0:
                stack.append(i)
                i += 1
            elif heights[stack[-1]] <= heights[i]:
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                if len(stack) != 0:
                    max_area = max(max_area, heights[top] * (i - stack[-1] - 1))
                else:
                    max_area = max(max_area, heights[top] * i)

        while len(stack) > 0:
            top = stack.pop()
            if len(stack) != 0:
                max_area = max(max_area, heights[top] * (i - stack[-1] - 1))
            else:
                max_area = max(max_area, heights[top] * i)

        return max_area
