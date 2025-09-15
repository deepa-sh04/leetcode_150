"""
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
Explanation:
Calculate effective rotations: k % n handles cases where k exceeds array length (prevents unnecessary full cycles).
Slicing:
nums[-k:] gets the last k elements (to be moved to front).
nums[:-k] gets all elements except the last k (to be placed after).
Rebuild array: nums[:] = ... modifies the list in-place (without creating a new reference).
Time Complexity: O(n)
Slicing operations each take O(n) time (copying elements).
Overall, the operation is linear relative to the input size.
"""
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n=len(nums)
        k=k%n
        nums[:]=nums[-k:]+nums[:-k]
        
        
