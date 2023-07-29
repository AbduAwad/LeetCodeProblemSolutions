class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_list = []

        if len(nums) == 0:
            num_list.append(-1)
            num_list.append(-1)
            return num_list

        for i in range(len(nums)):
            if nums[i] == target:
                num_list.append(i)
            elif target not in nums:
                num_list.append(-1)
                num_list.append(-1)
                break
        if len(num_list) == 1:
            num_list.append(num_list[0])

        num_list_final = []
        if len(num_list) > 2:
            num_list_final.append(min(num_list))
            num_list_final.append(max(num_list))
            return num_list_final
        else:
            return num_list