class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(0, len(nums)):
            if count not in nums:
                return count
            count += 1
        return count