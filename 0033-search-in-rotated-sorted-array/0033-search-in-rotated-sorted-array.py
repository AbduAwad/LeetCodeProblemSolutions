class Solution(object):
    def search(self, nums, target): # find pivot using binary search:(min value)
        left, right = 0, len(nums)-1
        pivotIdx = left + ((right - left) // 2)
        pivot = nums[pivotIdx]
        while left <= right:
            index = left + ((right - left) // 2)
            if (nums[index] == target):
                return index
            if nums[index] < pivot:
                pivotIdx = index
                pivot = nums[index]
            if (nums[index] > nums[right]): # min is in right half
                left = index + 1
            else: # min is in left half
                right = index - 1
        if nums[left] < pivot:
            pivotIdx = left
            pivot = nums[left]
        if target > nums[len(nums)-1]:
            left, right = 0, pivotIdx
        elif target > pivot:
            left, right = pivotIdx, len(nums)-1
        elif target == nums[pivotIdx]:
            return pivotIdx

        while left <= right: # binary serch in window from pivot to end or start based on where target is
            index = left + ((right - left) // 2)
            if nums[index] > target:
                right = index - 1
            elif nums[index] < target:
                left = index + 1
            else:
                return index
        return -1