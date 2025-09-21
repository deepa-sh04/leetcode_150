"""
Input: s = "abc", t = "ahbgdc"
Output: true
Two-pointer scan: move through t, advance i when s[i]==t[j].
If i reaches len(s), return True else False.
Time: O(len(t))
Space: O(1)
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        j=0
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
            j+=1
        if i==len(s):
            return True
        else:
            return False            

