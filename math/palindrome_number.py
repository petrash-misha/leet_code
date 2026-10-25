# 9. Palindrome Number
#
# Given an integer x, return true if x is a palindrome, and false otherwise.
#
# Example 1:
#
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
#
# Example 2:
#
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
#
# Example 3:
#
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#
# Constraints:
#
# -231 <= x <= 231 - 1
#
# Follow up: Could you solve it without converting the integer to a string?

class Solution:
    def isPalindrome(self, x: int) -> bool:
        import math
        # if x < 0:
        #     return False
        # x = str(x)
        # if len(x) % 2 == 0:
        #     middle = len(x) // 2
        # elif len(x) % 2 != 0:
        #     middle = int(len(x) // 2) + 1

        # for i in range(middle):
        #     if x[i] != x[-i - 1]:
        #         return False
        # return True

        if x < 0:
            return False

        if x == 0:
            return True

        place_value = int(math.log(x, 10))
        n = x
        while n > 0:
            left_num = (x // (10 ** place_value)) % 10
            right_num = n % 10
            if left_num != right_num:
                return False
            n //= 10
            place_value -= 1
        return True