#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            return sorted(s) == sorted(t)
        return False
        
# @lc code=end
