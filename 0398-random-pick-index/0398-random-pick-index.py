import random

class Solution(object):
    
    def __init__(self, nums):
        self.map = {}
        for i in range(len(nums)):
            if self.map.get(nums[i]) != None:
                self.map.get(nums[i]).append(i)
            else:
                self.map[nums[i]] = [i]

    def pick(self, target):
        return self.map[target][random.randint(0, len(self.map[target])-1)]

# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)