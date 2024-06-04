class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxSeq = 0
        currSeq = 0
        for num in numSet:
            if (num  - 1) not in numSet:
                currSeq = 1
                while (num + currSeq) in numSet:
                    currSeq += 1
                if currSeq > maxSeq:
                    maxSeq = currSeq
        return maxSeq
