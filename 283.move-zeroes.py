#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        while True:
            try:
                nums.remove(0); count += 1
            except:
                break
        for i in range(count):
            nums.append(0)
# @lc code=end
