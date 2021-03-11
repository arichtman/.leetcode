#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#
from __future__ import annotations
# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = i = 0
        # I'm settling for the <= 'hack' here over the != as it just wasn't behaving.
        for i in range(32):
            count += (0, 1)[(n ^ (1 << i)) <= n]
        return count
        
# @lc code=end

sol = Solution()
print(sol.hammingWeight(123456789))

# May work complementing the mask, then running a regular and between the two but I'm happy for now.
