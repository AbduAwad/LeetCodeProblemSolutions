class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers) - 1
        while start < end:
            if (numbers[start] + numbers[end] == target):
                return [start+1,end+1]
            if (numbers[start] + numbers[end] < target):
                start += 1
            else: # greater than the target:
                end -= 1