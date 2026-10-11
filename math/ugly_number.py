# 263. Ugly number
#
# An ugly number is a positive integer which does not have a prime factor other than 2, 3, and 5.
#
# Given an integer n, return true if n is an ugly number.
#
# Example 1:
#
# Input: n = 6
# Output: true
# Explanation: 6 = 2 × 3
#
# Example 2:
#
# Input: n = 1
# Output: true
# Explanation: 1 has no prime factors.
#
# Example 3:
#
# Input: n = 14
# Output: false
# Explanation: 14 is not ugly since it includes the prime factor 7.
#
# Constraints:
#
# -231 <= n <= 231 - 1

def is_not_dev_235(f):
    if f % 2 != 0 and f % 3 != 0 and f % 5 != 0:
        return True
    return False

class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        if n < 7:
            return True
        if is_not_dev_235(n):
            return False

        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                if is_not_dev_235(i) or is_not_dev_235(n / i):
                    return False

        return True