class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        # Three Sum: No Duplicates, Any order, such that x + y + z = 0
        # in other words, x + y = -z
        # Sort nums
        nums = sorted(nums)
        # Set needed vars
        triplets = []

        for i in range(len(nums) - 2): # i = index; end needs to be last index - 2
            # preliminary checks: positives can't add up to zero
            if nums[i] > 0:
                break
            
            # check PREVIOUS number; if duplicate, continue to next number
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left, right = i+1, len(nums)-1
            target = 0 - nums[i]
            while left < right: # goes to middle
                if nums[left] + nums[right] == target: # successful triplet
                    triplets.append([nums[left], nums[right], nums[i]])

                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -=1

                    left+=1
                    right-=1
                elif nums[left] + nums[right] < target: # too small; needs left to be greater
                    left+=1
                else: # too high; needs right to be less
                    right-=1
        return triplets
