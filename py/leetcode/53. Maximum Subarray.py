# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/description/
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# Example:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

# Example 2:

# Input: nums = [1]
# Output: 1

# solution 1 brute force:
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        length = len(nums)
        if length <= 1:
            return nums
        totalSum = -math.inf
        for i in range(length):
            currentSubSum = 0
            for j in range(i, length):
                currentSubSum += nums[j]
                totalSum = max(totalSum, currentSubSum)
        return totalSum
# the solution above has O(n^2) time complexity

# optimized solution:
# Whenever the sum of the array is negative, we know the entire array is not worth keeping, so we'll reset it back to an empty array.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        totalSum = currentSum = num[0]
        for num in nums[1:]:
            currentSum += num
            totalSum = max(totalSum, currentSum)
            if currentSum < 0:
                currentSum = 0
            # instead of this for loop, we can also use the following:
            # currentSum = max(num, currentSum + num)
            # totalSum = max(totalSum, currentSum)
        return totalSum

class Solution:
    def maxSubArray(self, nums):
        currentSub = maxTotal = nums[0]
        for num in nums[1:]:
            currentSub += num
            maxTotal = max(maxTotal,currentSub)
            if currentSub < 0:
                currentSub = 0
        return maxTotal


