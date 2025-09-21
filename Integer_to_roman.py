"""
Input: num = 3749
Output: "MMMDCCXLIX"

The code changes a number into Roman letters step by step:
Big to small list – It keeps a list of Roman values and their letters from 1000 (“M”) down to 1 (“I”).
Go through each pair – For each value:
If your number is still that big, subtract it and add the matching letter to the answer.
Repeat until the number is smaller than that value.
Keep moving down the list until the number becomes 0.
Return the letters you collected.
Time: O(number of symbols)
Space: O(1) besides the output string.
"""
class Solution:
    def intToRoman(self, num: int) -> str:
      mape=[
        (1000,'M'),
        (900,'CM'),
        (500,'D'),
        (400,'CD'),
        (100,'C'),
        (90,'XC'),
        (50,'L'),
        (40,'XL'),
        (10,'X'),
        (9,'IX'),
        (5,'V'),
        (4,'IV'),
        (1,'I')
    
       ]
      result=""
      for value,symbol in mape:
        while num>=value:
            num-=value
            result+=symbol
      return result           
