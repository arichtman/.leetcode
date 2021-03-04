#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (l1 is None):
            return l2
        elif (l2 is None):
            return l1
        stack = []
        stack += self.flattenList(l1)
        stack += self.flattenList(l2)
        stack = sorted(stack)

        firstNode = ListNode(stack[0])
        lastNode = firstNode
        for i in range(len(stack)-1):
            lastNode.next = ListNode(stack[i+1])
            lastNode = lastNode.next
        return firstNode

    def flattenList(self, startingNode: ListNode) -> List:
        stack = []
        while startingNode is not None:
            stack.append(startingNode.val)
            startingNode = startingNode.next
        return stack
# @lc code=end
