#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
from __future__ import annotations
# @lc code=start
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        for row in range(numRows):
            pascalRow = []
            for i in range(row+1): # Can stop at half way and reverse the digits due to symmetry
                pascalRow.append(self.pascalNum(row, i))
            triangle.append(pascalRow)
        return triangle
# I am well aware that this recurses unnecessarily - to be improved
    def pascalNum(self, depth: int, place: int) -> int:
        if place == 0: # Stop recursion before negative places
            return 1
        # Casting to int is occasionally out due to tiny variation around the actual digits
        return round(((depth + 1 - place) / place) * self.pascalNum(depth, place - 1))
# @lc code=end

sol = Solution()
print(sol.generate(15))