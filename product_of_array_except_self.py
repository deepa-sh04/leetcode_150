"""
Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
explanation::-
Logic:
Make one pass left→right storing product of all left elements.
Make one pass right→left multiplying product of all right elements.

Time: O(n)
Space: O(1) extra (O(n) for result array).
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        pro=[1]*n
        prefix=1
        for i in range(n):
            pro[i]*=prefix
            prefix*=nums[i]
        suffix=1
        for i in range(n-1,-1,-1):
            pro[i]*=suffix
            suffix*=nums[i]
        return pro        
