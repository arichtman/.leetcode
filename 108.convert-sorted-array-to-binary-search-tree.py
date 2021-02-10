#
# @lc app=leetcode id=108 lang=python3
#
# [108] Convert Sorted Array to Binary Search Tree
#
from __future__ import annotations

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        return self.subRoutine(nums)

    def subRoutine(self, nums: List[int]) -> TreeNode:
        medianIndex = len(nums)//2
        root = TreeNode(nums[medianIndex])
        if len(nums) > 1:
            root.left = self.subRoutine(nums[:medianIndex])
            if len(nums) > 2:
                root.right = self.subRoutine(nums[medianIndex+1:])
        return root
# @lc code=end

sol = Solution()
root = sol.sortedArrayToBST([-10,-3,0,5,9])
