#
# @lc app=leetcode id=171 lang=python3
#
# [171] Excel Sheet Column Number
#

# @lc code=start
class Solution:
    def titleToNumber(self, s: str) -> int:
        total = 0
        for index, char in enumerate(s[::-1]):
            total += (ord(char)-64)*pow(26, index)
        return total
        # return sum(map(lambda x: (ord(x[1])-64)*pow(26, x[0]), enumerate(s[::-1])))
# @lc code=end
