class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            index = left + ((right - left) // 2)
            if (nums[index] < target):
                left = index + 1
            elif (nums[index] > target):
                right = index - 1
            else:
                return index
        return -1