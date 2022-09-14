# 2. Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    curr = dummy
    
    carry=0
    
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        val = val1 + val2 + carry
        carry, val = divmod(val,10)
        
        curr.next = ListNode(val)
        
        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    return dummy.next

# solution 2


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = ListNode(None)
        pointer = ans

        carry = 0
        sum = 0

        while (l1 != None or l2 != None):
            sum = carry
            if (l1 != None):
                sum += l1.val
                l1 = l1.next
            if (l2 != None):
                sum += l2.val
                l2 = l2.val

            carry = int(sum/10)
            pointer.next = ListNode(sum % 10)

            pointer = pointer.next

        if (carry > 0):
            pointer.next = ListNode(carry)

        return ans.next
