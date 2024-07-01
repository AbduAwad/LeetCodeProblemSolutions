class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        oddCount = 0
        for num in arr:
            if oddCount == 3:
                return True
            if num % 2 != 0:
                oddCount += 1
            else:
                oddCount = 0
        return oddCount == 3