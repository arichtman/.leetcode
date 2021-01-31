#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
      nums.sort()
      i = 0
      nums.append((3 * 10**4) + 1)
      while nums[i] == nums[i+1]:
        i+=2
      return nums[i]
# @lc code=end

test_list = [1, 5, 3, 6, 3, 5, 6, 1, 9]
dups = {}
[ dups[i] = dups[i]+1 for i in test_list ]
[i for n, i in enumerate(test_list) if dups[i] < 1 ]

test_list = [1, 5, 3, 6, 3, 5, 6, 1, 9]
test_list.sort()
i = 0
test_list.append((3 * 10**4) + 1)
while test_list[i] == test_list[i+1]:
  i+=2
return test_list[i]