#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def __init__(self):
    self.maxHeight = 0

  def maxDepth(self, root: TreeNode) -> int:
    self.doThing(root, 0)
    return self.maxHeight
  
  def doThing(self, node: TreeNode, depth):
    if node:
      self.doThing(node.left, depth+1)
      self.doThing(node.right, depth+1)
    else:
      self.maxHeight = max(self.maxHeight, depth)

# @lc code=end

root = [3,9,20,None,None,15,7]

breadCrumbs = []
currentNode = 0
maxDepth = 0

nextNode = currentNode + (len(breadCrumbs)+1)
if root[nextNode] is not None:
    breadCrumbs.append(currentNode)
    currentNode = nextNode
else:
    nextNode = currentNode + (len(breadCrumbs)+2)
    if root[nextNode] is not None:
        breadCrumbs.append(currentNode)
        currentNode = nextNode
    else:
        maxDepth = max(maxDepth, len(breadCrumbs))
        offSet = (len(breadCrumbs)+1)
        currentNode = breadCrumbs.pop() + offSet


#Pseudo code

get current node index
calculate next left node index
if not null push current node to stack, set next node to left index
else null calculate right node index
if right node value not null push current node to stack, set next node to right index
if both null compare and set max depth if length of stack exceeds existing value
then pop stack value, set next node to that index

root = [ 'a', 'b', 'c', None, 'd', 'e', None, None, None, None, None, 'g', None, None, None ]
if root is None:
  return 0
else:
  root.reverse()
  maxIndex = len(root) - root.index(next(filter(lambda x: x!= None, root)))

  while maxIndex != 0:
      maxIndex = (maxIndex - 1) // 2
      depth += 1
  return depth+1
