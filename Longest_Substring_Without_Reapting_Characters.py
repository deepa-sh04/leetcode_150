"""
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
BY using sliding window concept and using while loop if the element is already present then move the window left, by adding left+=1
Time Complexity: O(n) (each character is added and removed at most once)
Space Complexity: O(min(n, charset size))
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        char_set = set()
        max_len = 0
        for right in range(len(s)):
            while s[right] in char_set:  
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len
