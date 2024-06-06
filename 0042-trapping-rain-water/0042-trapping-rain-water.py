class Solution:
    def trap(self, height: List[int]) -> int:            
        left = 0
        right = len(height) - 1   
        maxLeft = height[left]
        maxRight = height[right]  
        water = 0
        while left < right:
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(height[left], maxLeft)
                water += maxLeft - height[left] 
            else:
                right -= 1
                maxRight = max(height[right], maxRight)
                water += maxRight - height[right]
        return water