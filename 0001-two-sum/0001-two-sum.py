class Solution(object):
    def twoSum(self, nums, target):
        numsMap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if (numsMap.get(complement) != None):
                return [i, numsMap.get(complement)]
            numsMap[nums[i]] = i