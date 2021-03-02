#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        replacements = (
            ('IV', 4),
            ('IX', 9),
            ('XL', 40),
            ('XC', 90),
            ('CD', 400),
            ('CM', 900)
        )
        for replacement in replacements:
            if s.find(replacement[0])>-1:
                s = s.replace(replacement[0],'')
                total += replacement[1]
        counts = (
            ('I', 1),
            ('V', 5),
            ('X', 10),
            ('L', 50),
            ('C', 100),
            ('D', 500),
            ('M', 1000)
        )
        for count in counts:
            total += (s.count(count[0])*count[1])
        return total
# @lc code=end

sol = Solution()
result = sol.romanToInt('XXIX')
print(result)