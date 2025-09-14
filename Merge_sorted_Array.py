"""
nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
given two array of size m and n we need merge it in sorted way.
🔹 Time Complexity

Loop (for i in range(n))
Runs n times → O(n)
sorted(nums1)
Length of nums1 is m + n
Sorting takes O((m+n)·log(m+n))
✅ Total Time Complexity = O(n) + O((m+n)·log(m+n)) = O((m+n)·log(m+n))

🔹 Space Complexity
nums1 is modified in place (no new array created for merging).
But sorted(nums1) creates a new sorted list, which takes O(m+n) extra space.
✅ Space Complexity = O(m+n)
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        for i in range(n):
            nums1[m+i]=nums2[i]
        nums1.sort() 
      



