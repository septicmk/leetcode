# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if root == None or p == None or q == None:
            return None
        def bet(ans, p, q):
            if ans.val > p.val and ans.val < q.val or ans.val > q.val and ans.val < p.val:
                return ans
            elif ans.val < p.val and ans.val < q.val:
                return bet(ans.right, p ,q)
            else:
                return bet(ans.left, p, q)

        def dfs(x,y):
            if x == y:
                return True
            elif x == None:
                return False
            return dfs(x.left,y) or dfs(x.right,y)

        if dfs(p,q):
            return p
        elif dfs(q,p):
            return q
        else:
            return bet(root, p ,q)



