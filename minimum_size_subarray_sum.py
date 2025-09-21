"""
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        curr_sum=0
        mini=float("inf")
        for right,num in enumerate(nums):
            curr_sum+=num
            while curr_sum>=target:
                mini=min(mini,right-left+1)
                curr_sum-=nums[left]
                left+=1
        return( 0 if mini==float("inf") else mini)        
