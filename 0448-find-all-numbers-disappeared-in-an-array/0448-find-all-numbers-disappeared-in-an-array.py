class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        n = set(nums)
        output = []
        for i in range(1, len(nums)+1):
            if i not in n:
                output.append(i)
        return output
        