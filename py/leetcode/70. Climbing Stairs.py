# 70. Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/description/
# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
# Note: Given n will be a positive integer.
#
# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

# memorization method:
class Solution:
    def __init__(self):
        self.dic = {1:1, 2:2}

    def climbStairs(self, n):
        if n not in self.dic:
            self.dic[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dic[n]

# clean recursive method:
class Solution:
    # Top down - TLE
    def climbStairs1(self, n):
        if n <= 2:
            return n
        return self.climbStairs(n-1)+self.climbStairs(n-2)

# buttom-up method:
class Solution:
    def climbStairs(self, n):
        if n <= 2:
            return n
        a, b = 1, 2
        for i in range(2, n):
            a, b = b, a+b
            # same as:         
            # tmp = b
            # b = a+b
            # a = tmp
        return b