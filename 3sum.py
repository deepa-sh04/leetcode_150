"""
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Explanation (short):
Sort the array.
For each index i, use two pointers (j left, k right) to find pairs where nums[i] + nums[j] + nums[k] == 0.
Skip duplicates for i, j, and k to avoid repeated triplets.
Time Complexity:
Sorting: O(n log n)
Outer loop + two-pointer scan: O(n²)
Overall: O(n²)
Space Complexity:
Sorting in place + a few variables → O(1) extra (excluding the output list).

"""
nums = [-1,0,1,2,-1,-4]
nums.sort()                     
ans = []
for i in range(len(nums)):
    if i > 0 and nums[i] == nums[i-1]:
        continue
    j, k = i + 1, len(nums) - 1
    while j < k:
        s = nums[i] + nums[j] + nums[k]
        if s == 0:
            ans.append([nums[i], nums[j], nums[k]])
            j += 1
            k -= 1
            while j < k and nums[j] == nums[j - 1]:
                j += 1
            while j < k and nums[k] == nums[k + 1]:
                k -= 1
        elif s < 0:
            j += 1
        else:
            k -= 1
print(ans)
