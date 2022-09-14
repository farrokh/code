# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Example 1:
# Input: head = [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]
# Example 2:


# Input: head = [1, 2]
# Output: [2, 1]
# Example 3:

# Input: head = []
# Output: []


# Constraints:
# The number of nodes in the list is the range[0, 5000].
# -5000 <= Node.val <= 5000

# solution

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node = None
        while (head is not None):
            next = head.next
            head.next = node
            node = head
            head = next
        return node
