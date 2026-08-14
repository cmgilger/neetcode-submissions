class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # need to know: width, minimum height (product: area)
        # goal: find MAX area
        # needed vars: max area, one and two (the indices), min(h_one, h_two), width
        # complexity: O(n) (i.e. one loop)
        max_area = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            area = (right - left) * min(heights[left], heights[right]) # area formula

            max_area = max(max_area, area)

            if heights[left] < heights[right]:
                left+=1 # if the left height is smaller, move it
            else:
                right-=1 # if the right height is smaller, move it
        return max_area