class Solution:
    def removeDuplicates(self, nums):
        nums_set = list(set(nums))
        nums_set.sort()
        return len(nums_set)
