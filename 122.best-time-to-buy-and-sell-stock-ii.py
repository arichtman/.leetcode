#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#
from __future__ import annotations
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ptr = 0
        prices.append(-1)
        haveMoney: bool = True
        totalProfit = 0
        maxIndex = len(prices)-1
        while ptr < maxIndex:
            if haveMoney:
                if prices[ptr+1] <= prices[ptr]:
                    ptr += 1
                else:
                    cost = prices[ptr]
                    haveMoney = False
            else:
                if prices[ptr+1] >= prices[ptr]:
                    ptr += 1
                else:
                    totalProfit += prices[ptr] - cost
                    haveMoney = True
        return totalProfit
        
# @lc code=end

nums = [7,1,5,3,6,4]
nums = [1,2,3,4,5]
sol = Solution()
sol.maxProfit(nums)
""" 
init ptr to index zero
init state already sold
if we've already sold we're looking to buy so local minimum
  if next value is lower or equal move ptr
  else
    cost = value at current pointer
    state to looking to sell

if we're looking to sell look for local maximum
  if next value is higher or equal move ptr
  else
    price = value at current pointer
    profit += price - cost
    state to already sold
recurse

I'm thinking about running off the end of the array as well as some edge case where there's a really good trade but we have to skip some initial small one to get the "rythm" right 
"""