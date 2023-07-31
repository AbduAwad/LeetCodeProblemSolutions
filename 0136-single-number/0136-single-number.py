class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        no_duplicate_list = list(set(nums))
        # Remove number that is not duplicate essentially.
        for i in range(0, len(no_duplicate_list)):
            if no_duplicate_list[i] in nums:
                nums.remove(no_duplicate_list[i])

        # Compare set of duplicates only with set of original list.
        return int(list(set(no_duplicate_list).symmetric_difference(set(nums)))[0])
