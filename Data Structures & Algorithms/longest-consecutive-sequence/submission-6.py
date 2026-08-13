class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # check for empty sequence
        if not nums:
            return 0
        
        # create set for nums (time saver)
        num_set = set(nums)
        # create max stream var
        max_streak = 0
        
        for num in num_set:
            # Only start counting from the beginning of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                # Count how far this sequence extends
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                max_streak = max(max_streak, current_streak)
        
        return max_streak
                
