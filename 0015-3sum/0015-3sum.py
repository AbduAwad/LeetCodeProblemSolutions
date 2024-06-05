class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # O(logn)
        output = [] # Then its a two sum on the remaining numbers O(n^2)
        for i in range(len(nums)):
            target = -1*nums[i] # To get 0 it will adding the complement
            left = i + 1
            right = len(nums) - 1
            # its sorted so if val > 0 as 1st # will never be -ve for numbers after
            if nums[i] > 0: 
                break
            if i > 0 and nums[i] == nums[i - 1]: # Skip the duplicate
                continue
            while left < right: # two-pointer approach
                if (nums[left] + nums[right]) > target:
                    right -= 1
                elif (nums[left] + nums[right]) < target:
                    left += 1
                else:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1 # move from current number
                    right -= 1 # movde from current number
                     # Skip the consecutive numbers to remove duplicates:
                    while nums[left] == nums[left - 1] and left < right: 
                        left += 1
        return output