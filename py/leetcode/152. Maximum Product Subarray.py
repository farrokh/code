# 152. Maximum Product Subarray
# Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.
# A subarray is a contiguous subsequence of the array.

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.

# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.


# solution 1 brute force O(n2):
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        length = len(nums)
        if length <1:
            return None
        max_product = nums[0]
        for i in range(length):
            curr_product = nums[i]
            max_product = max(max_product,curr_product)
            for j in range(i+1,len(nums)):
                curr_product *= nums[j]
                max_product = max(max_product,curr_product)
        return max_product

# dynamic programming solution:
# trick here is to keep track of both min and max on each index and compare the current max to result at each index. 0 is the edge case but since we check the number alongside the current max and min, we will be fine (currentMax = max(num,currentMax*num,currentMin*num)). don't forget to use temp variable to store currentMax at the beginning of each iteration.

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # error checking:
        if not nums:
            return 0

        # set variables:
        currMax = currMin = result = nums[0]
        
        # Loop through numbers:
        for num in nums[1:]:
            tempMaxSoFar = max(num, num*currMax, num*currMin)
            currMin = min(num, num*currMax, num*currMin)
            currMax = tempMaxSoFar
            
            result=max(result,currMax)
        
        # return result:
        return result
            