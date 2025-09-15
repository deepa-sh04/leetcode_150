""""
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49
Use two pointers (left and right).
Calculate area: min(height[left], height[right]) * (right - left).
Move the pointer with the smaller height inward (to seek a taller line).
Track maximum water.

Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left=0
        water=0
        right=len(height)-1
        for i in range(len(height)):
            if height[left]>height[right]:
                water=max(water,(min(height[left],height[right]))*(right-left))
                right-=1
            else:
                water=max(water,(min(height[left],height[right]))*(right-left))
                left+=1
        return water 
     
