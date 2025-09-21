"""
Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.

Trim spaces, split into words, and return the length of the last word (0 if none).
Time: O(n) — one pass to strip/split.
Space: O(n) — stores the words list.
"""
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words=s.strip().split()
        if not words:
            return 0
        return len(words[-1])    
