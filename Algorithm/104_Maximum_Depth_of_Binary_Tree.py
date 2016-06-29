# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        def func(node, dept):
            if node == None:
                return dept
            elif node.left == None and node.right == None:
                return dept + 1
            else :
                return 1 + max(func(node.left, dept), func(node.right, dept))
        return func(root,0)
