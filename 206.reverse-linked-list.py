#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pastNode = None
        currentNode = head
        while currentNode is not None:
          nextNode = currentNode.next
          currentNode.next = pastNode
          pastNode = currentNode
          currentNode = nextNode
        return pastNode

# @lc code=end

Pseudo

get next node reference
set head node next to null
set next node reference to head
move to next node
store next node reference
update object to point to previous node

