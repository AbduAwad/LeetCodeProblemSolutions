class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        alr_seen = set()
        
        for num in nums:
            alr_seen.add(num)

        if len(alr_seen) != len(nums):
            return True
        return False
                
