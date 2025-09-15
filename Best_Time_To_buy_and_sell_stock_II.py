"""
Input: prices = [7,1,5,3,6,4]
Output: 7
Initialize profit to 0 (to accumulate total profit).
Iterate from the second day to the last day (index 1 to len(prices)-1):
For each day i, compare the price with the previous day (prices[i-1] and prices[i]).
If the current price is higher than the previous day (prices[i-1] < prices[i]), it means there is a profit opportunity from buying the previous day and selling today.
Add the difference (prices[i] - prices[i-1]) to profit.
Return the total accumulated profit.
Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        for i in range(1,len(prices)):
            if prices[i-1]<prices[i]:
                profit+=(prices[i]-prices[i-1])
        return profit        
        
