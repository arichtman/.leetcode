#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#
from __future__ import annotations
# @lc code=start
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return self.triangularNumber(len(nums)) - sum(nums)

    def triangularNumber(self, num: int) -> int:
        return round((num * (num+1))/2)

# @lc code=end

nums = [9,6,4,2,3,5,7,0,1]
sol = Solution()
print(sol.missingNumber(nums))
