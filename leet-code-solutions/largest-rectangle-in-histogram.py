class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(float("-inf"))
        n = len(heights)
        area = 0
        stack = [(0, -1)]

        for i in range(1, n):
            cur_lb = i - 1
            while stack and heights[stack[-1][0]] > heights[i]:
                idx, lb = stack.pop()
                cur_lb = lb
                area = max(area, heights[idx] * (i - lb - 1))

            stack.append((i, cur_lb))

        return area

        