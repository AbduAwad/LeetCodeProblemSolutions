class Solution(object):
    def productExceptSelf(self, nums):
        num,num2 = 1,1
        prefixArr,suffixArr = [],[]
        for i in range(0, len(nums) - 1):
            num *= nums[i]
            prefixArr.append(num)
        for x in range(len(nums) - 1, 0, -1):
            num2 *= nums[x]
            suffixArr.append(num2)

        output = []
        lenNums = len(nums)
        for i in range(lenNums):
            if (i == 0):
                prefix = 1
            else:
                prefix = prefixArr[i - 1]   
            if (i == (lenNums - 1)):
                postfix = 1
            else:
                postfix = suffixArr[lenNums - i - 2]
            output.append(prefix*postfix)
        return output
            
