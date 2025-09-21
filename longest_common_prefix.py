"""
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

explanation:-
Sort the list, compare only the first and last strings, and build the common prefix until characters differ.
Time: O(m log n + k)
Sorting: m log n where n = number of strings, m = average length.
Prefix check: k = length of shortest string.
Space: O(1) extra (ignoring sort’s internal use).
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        stre=sorted(strs)
        present=""
        stre1=stre[0]
        stre2=stre[-1]
        for i in range(min(len(stre1),len(stre2))):
            if stre1[i]!=stre2[i]:
                break
            else:
                present+=(stre1[i])
        return present            
