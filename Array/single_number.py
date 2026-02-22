# 136. Single Number
#
# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
#
# You must implement a solution with a linear runtime complexity and use only constant extra space.
#
# Example 1:
# Input: nums = [2, 2, 1]
# Output: 1
#
# Example 2:
# Input: nums = [4, 1, 2, 1, 2]
# Output: 4
#
# Example 3:
# Input: nums = [1]
# Output: 1
#
# Constraints:
#
# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
#
# Each element in the array appears twice except for one element which appears only once.

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        total = 0
        for i in nums:
            total ^= i

        return total

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        count_array = []
        num_array = []
        highest_num = 0
        lowest_num = 0

        for i in range(len(nums)):
            if nums[i] > highest_num:
                highest_num = nums[i]
            if nums[i] < lowest_num:
                lowest_num = nums[i]

        if lowest_num >= 0:
            count_array = [0] * (highest_num + 1)
            num_array = [0] * (highest_num + 1)
        else:
            count_array = [0] * (highest_num + abs(lowest_num) + 1)
            num_array = [0] * (highest_num + abs(lowest_num) + 1)

        for num in nums:
            count_array[num] += 1
            num_array[num] = num

        for i in range(len(count_array)):
            if count_array[i] == 1:
                return num_array[i]
