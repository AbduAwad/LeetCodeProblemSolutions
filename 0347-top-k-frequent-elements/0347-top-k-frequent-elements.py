class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dict_nums = {}
        for num in nums:
            dict_nums[num] = dict_nums.get(num, 0) + 1

        max_value = 0
        max_key = None
        max_key_list = []

        for i in range(0, k):
            for key, value in dict_nums.items():
                if value > max_value:
                    max_key = key
                    max_value = value
            del dict_nums[max_key]
            max_key_list.append(max_key)
            max_value = 0
        return max_key_list