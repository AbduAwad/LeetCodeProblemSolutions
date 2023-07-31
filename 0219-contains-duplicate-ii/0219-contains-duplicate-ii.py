class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        nums_set = set(nums)
        
        if len(nums) == len(nums_set):
            return False
        
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j] and j - i <= k:
                    return True