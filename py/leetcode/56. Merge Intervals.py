# 56. Merge Intervals
# https://leetcode.com/problems/merge-intervals/description/
# Given a collection of intervals, merge all overlapping intervals.
# Example 1:
#   Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
#   Output: [[1,6],[8,10],[15,18]]
#   Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x : x[0]) #O(nlogn)
        myList = []
        for items in intervals:
            if len(myList)==0:
                myList.append(items)
            else:
                if items[0]<=myList[-1][1] and items[1]>myList[-1][1]:
                    newRange = (myList[-1][0],items[1])
                    myList.pop()
                    myList.append(newRange)
                elif items[1]>myList[-1][1]:
                    myList.append(items)
        return myList