# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helper(-float("inf"),root,float("inf"))
    def helper(self, low, root, high):
        '''
        :type   low: int
                root: TreeNode
                high: int
        :rtype:bool
        '''
        if root == None: return True
        
        left_res = self.helper(low, root.left, root.val)
        right_res = self.helper(root.val, root.right, high)
        return low < root.val < high and left_res and right_res
        