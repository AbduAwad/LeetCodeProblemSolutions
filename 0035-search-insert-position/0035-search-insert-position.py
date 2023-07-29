class Solution(object):
    def searchInsert(self, nums, target):
    
        temp = 0
        while True:
            flag = True
            i = 0
            while i < (len(nums)):
                if nums[i] == target:
                    return i
                    flag = False
                i += 1

            if flag == False:
                break

            nums.append(target)
            for x in range(len(nums)): #To go through the list through the number of element times
                for i in range(1, len(nums)): # Goes through the list
                    if nums[i-1] > nums[i]: #If list item at the previous position is greater then switch spots
                        temp = nums[i]
                        nums[i] = nums[i - 1]
                        nums[i - 1] = temp
            print(nums)

