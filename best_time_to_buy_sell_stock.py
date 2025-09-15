"""
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation:
Initialize:
maxi = 0 (maximum profit so far)
buy = infinity (minimum buying price encountered so far)
Iterate through each price:
If the current price i is lower than buy, update buy to i (found a cheaper buying point).
Otherwise, calculate profit i - buy and update maxi if this profit is larger.
Return maximum profit (maxi).
Time Complexity: O(n)
Single pass through the list (prices), each operation is O(1) per element.
Space Complexity: O(1
Only constant extra variables (maxi, buy) are used.
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
      maxi=0
      buy=float("inf")
      for i in prices:
        if buy>i:
            buy=i
        maxi=max(maxi,i-buy)   
      return maxi   
