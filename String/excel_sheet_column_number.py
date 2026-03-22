# 171. Excel column sheet numbers
#
# Given a string columnTitle that represents the column title as appears
# in an Excel sheet, return its corresponding column number.
#
# For example:
#
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...
#
# Example 1:
#
# Input: columnTitle = "A"
# Output: 1
#
# Example 2:
#
# Input: columnTitle = "AB"
# Output: 28
#
# Example 3:
#
# Input: columnTitle = "ZY"
# Output: 701
#
# Constraints:
#
# 1 <= columnTitle.length <= 7
# columnTitle
# consists
# only
# of
# uppercase
# English
# letters.
# columnTitle is in the
# range["A", "FXSHRXW"].
#

def digit(letter):
    return ord(letter) - 64


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        p = len(columnTitle) - 1
        for current_letter in columnTitle:
            res += digit(current_letter) * (26 ** p)
            p -= 1

        return res

