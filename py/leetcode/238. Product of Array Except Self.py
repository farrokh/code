# 238. Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# others solution (a little faster):
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            res[i]=prefix
            prefix *=nums[i]
        
        posfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= posfix
            posfix *=nums[i]
        
        return res

# my solution:
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        prefsProd = []
        suffsProd = []
        length = len(nums)
        for i in range(length):
            if(i==0):
                product = 1
            else:
                product = product * nums[i-1]
            
            prefsProd.append(product)
        
        i=length-1
        while i>=0:
            if(i==length-1):
                product = 1
            else:
                product = product * nums[i+1]
            
            suffsProd.append(product)
            i-=1
        
        k=0        
        while k< length:
            answer.append(prefsProd[k]*suffsProd[-k-1])
            k+=1
        return answer

# a cleaner my solution
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        prefsProd = []
        suffsProd = []
        length = len(nums)
        product = 1
        for i in range(length):
            prefsProd.append(product)
            product = product * nums[i]
        
        product = 1
        i=length-1
        while i>=0:
            suffsProd.append(product)
            product = product * nums[i]
            i-=1
        
        k=0        
        while k< length:
            answer.append(prefsProd[k]*suffsProd[-k-1])
            k+=1
        return answer