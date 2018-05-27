# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        Wrong for some reason 
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.helper(nums)
        
    def helper(self,nums):
        if len(nums) == 0: 
            return None
        if len(nums) == 1: 
            res = TreeNode(nums[0])
            return res
        if len(nums) == 2:
            res = TreeNode(nums[0])
            res.right == self.helper(nums[1:-1])
            return res
            
        res = TreeNode(nums[len(nums)//2])
        res.left = self.helper(nums[0:len(nums)//2])
        res.right = self.helper(nums[len(nums)//2+1:len(nums)-1])
        return res 


        
class Solution:
    # @param num, a list of integers
    # @return a tree node
    # 12:37
    def sortedArrayToBST(self, num):
        if not num:
            return None

        mid = len(num) // 2

        root = TreeNode(num[mid])
        root.left = self.sortedArrayToBST(num[:mid])
        root.right = self.sortedArrayToBST(num[mid+1:])

        return root