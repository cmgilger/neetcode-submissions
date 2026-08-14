class Solution:
    def trap(self, height: List[int]) -> int:
        # return total water "trapped" between bars; in other words, the area
        total_area = 0

        # Step 1: Prefix maximum array
        prefix_max = []
        curr_max = 0 
        for i in height: # prefix maximum
            curr_max = max(curr_max, i) # sets new max
            prefix_max.append(curr_max) # adds current max to array on every pass

        # Step 2: suffix maximum array
        suffix_max = []
        curr_max = 0
        reversed_height = height[::-1]
        for i in reversed_height: # suffix maximum
            curr_max = max(curr_max, i)
            suffix_max.append(curr_max)
        
        suffix_max = suffix_max[::-1] # right way around

        # Step 3: find max water by square, sum it up
        for i, h in enumerate(height):
            water = min(prefix_max[i], suffix_max[i]) - h
            total_area += water

        # Step 4: return total
        return total_area