# 217. Contains Duplicate
# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
# Example 1:
# Input: nums = [1,2,3,1]
# Output: true

# Example 2:

# Input: nums = [1,2,3,4]
# Output: false

# my solution (easier and faster):
from collections import defaultdict
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) - len(set(nums))>0 :
            return True
        else:
            return False

# hash table solution:
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashedList = {}
        for i,num in enumerate(nums):
            if num not in hashedList:
                hashedList[num] = i
            else:
                return True
        return False


# default dic sotulion:
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        m = defaultdict(int)

        for num in nums:
            if m[num]:
                return True
            m[num] += 1
        return False
