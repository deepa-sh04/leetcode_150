"""
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Track farthest reach (j) and current jump end (curr).
When i reaches curr, jump and update curr = j.
Count jumps.
Time: O(n)
Space: O(1)
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        count=0
        j=0
        curr=0
        for i in range(len(nums)-1):
            j=max(j,i+nums[i])
            if i==curr:
                count+=1
                curr=j
        return count        
      
