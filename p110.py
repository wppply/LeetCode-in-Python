# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.height_helper(root, True)[1]
    
    def height_helper(self, root, flag):
        if not root: return 0, True
        
        l, f1 = self.height_helper(root.left, flag)
        r, f2 = self.height_helper(root.right, flag)
        
        flag = (f1 and f2) and (abs(l-r) <= 1)
        return max(l,r)+1, flag
        