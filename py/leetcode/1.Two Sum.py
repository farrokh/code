# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.


# Example 1:

# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3, 2, 4], target = 6
# Output: [1, 2]
# Example 3:

# Input: nums = [3, 3], target = 6
# Output: [0, 1]


# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

def twoSum(numbers,target):
    hashedList = {}
    for i,num in enumerate(numbers):
        n = target - num
        if n not in hashedList:
            hashedList[num] = i
        else:
            return [hashedList[n],i]

print(twoSum([2,7,11,15],9))


# solution 2:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        n = len(nums)
        for i in range(0, n):
            goal = target - nums[i]
            if (goal in m):
                return [m[goal], i]
            m[nums[i]] = i
