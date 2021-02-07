#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
  def fizzBuzz(self, n: int) -> List[str]:
    stack = []
    for i in range(1,n+1):
      a = ("Fizz", "" )[i % 3 > 0 ]
      b = ("Buzz", "" )[i % 5 > 0 ]
      stack.append( (a + b) or str(i))
    return stack
# @lc code=end

n = 15

stack = []
for i in range(1,n+1):
  a = ("Fizz", "" )[i % 3 > 0 ]
  b = ("Buzz", "" )[i % 5 > 0 ]
  stack.append( (a + b) or str(i))

stack = []
for i in range(1,n+1):
  a = "" if i % 3 else "Fizz"
  b = "" if i % 5 else "Buzz"
  stack.append( (a + b) or str(i))
return stack
