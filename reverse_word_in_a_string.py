"""
Input: s = "the sky is blue"
Output: "blue is sky the"


Split the string into words, trim spaces, reverse the list, and join with a single space.
Time: O(n) — splitting, reversing, and joining all scan the string once.
Space: O(n) — list of words plus output string.
"""
class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.strip().split()
        words.reverse()
        return (" ".join(words))
        
