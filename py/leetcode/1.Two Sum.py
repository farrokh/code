# 1. Two Sum
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# Example:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

def twoSum(numbers,target):
    hashedList = {}
    for i,num in enumerate(numbers):
        n = target - num
        if n not in hashedList:
            hashedList[num] = i
        else:
            return [hashedList[n],i]

print(twoSum([2,7,11,15],9))