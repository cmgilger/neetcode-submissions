class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # create prefix and suffix lists (pre-allocating)
        leftArr = [1] * n
        rightArr = [1] * n
        # fill arrays
        # left array: all elements to the left
        for i in range(1, n):
            leftArr[i] = leftArr[i-1] * nums[i-1]
        # right array: all elements to the right
        for i in range(n-2, -1, -1): # start, stop, step
            rightArr[i] = rightArr[i+1] * nums[i+1]

        prodList = [leftArr[i] * rightArr[i] for i in range(n)]
        return prodList
                    