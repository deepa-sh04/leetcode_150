"""
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Initialize reachable to 0 (farthest index we can reach so far).
Iterate through each index i and jump value jump:
If current index i is beyond reachable → cannot proceed → return False.
Update reachable = max(reachable, i + jump) (how far we can jump from here).
If we complete the loop, return True (reached the end).
Time Complexity: O(n)
Single pass through the array.
Space Complexity: O(1)
Only uses constant extra variables (reachable).
Greedy approach: Tracks the maximum reachable index at each step
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reachable=0
        for i,jump in enumerate(nums):
            if i>reachable :
                return False
            reachable=max(reachable,i+jump)
        return True        
                         
        

