# Given the head of a linked list, remove the nth node from the end of the list and return its head.


# Example 1:


# Input: head = [1, 2, 3, 4, 5], n = 2
# Output: [1, 2, 3, 5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1, 2], n = 1
# Output: [1]


# Constraints:

# The number of nodes in the list is sz.
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        ans = ListNode(0)
        ans.next = head

        first = ans
        second = ans

        for i in range(1, n+2):
            first = first.next

        while (first is not None):
            first = first.next
            second = second.next

        second.next = second.next.next

        return ans.next
