class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxWater = 0
        while left < right:
            if (height[left] > height[right]):
                h = height[right]
            else:
                h = height[left]
            water = h * (right - left)
            if (water > maxWater):
                maxWater = water
            if (height[left] < height[right]):
                left += 1
            else:
                right -= 1
        return maxWater