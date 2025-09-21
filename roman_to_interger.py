"""
Input: s = "III"
Output: 3
Explanation: III = 3.
Loop through each Roman symbol, subtract its value if it’s smaller than the next one, otherwise add it.

Time: O(n) — single pass over the string.
Space: O(1) — fixed dictionary and a few variables
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
             'C': 100, 'D': 500, 'M': 1000}
        got=0
        for i in range(len(s)):
            if s[i] in roman.keys():
                if i+1<len(s) and roman[s[i]]<roman[s[i+1]]:
                    got-=roman[s[i]]
                else:
                    got+=roman[s[i]]
        return got                
