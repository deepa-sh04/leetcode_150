"""
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
It finds two numbers that add up to target:
Make a dictionary seen to remember each number’s index.
For every number num:
Compute comp = target - num (the partner we need).
If comp is already in seen, we found the pair → return their 1-based positions.
Otherwise store this number and its index in seen.

Time: O(n) – one pass through the list.
Space: O(n) – dictionary to store seen numbers.
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen={}
        for i,num in enumerate(numbers):
            comp=target-num
            if comp in seen:
                result=[seen[comp] + 1, i + 1]
                break
            seen[num]=i
        return result        
