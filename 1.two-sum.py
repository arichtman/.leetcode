#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return list(filter(None, [ [ [ firstIndex, firstIndex + 1 + secondIndex ] for secondIndex, secondNum in enumerate(nums[firstIndex+1:]) if ( firstNum + secondNum == target) ] for firstIndex,firstNum in enumerate(nums) ] ))[0][0]
# @lc code=end

