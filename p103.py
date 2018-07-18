# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = list()
        self.BFS([root], res)
        return res

    def BFS(self, line, res):
    	a = 1
    	while line:
    		node_line = list()
    		for n in line:
    			if n : 
    				node_line.append(n.left)
    				node_line.append(n.right)
    		val_line = [n.val for n in line]
    		if a == 1: res.append[val_line]
            else: res.append[val_line[::-1]]
            a = -a
    		line = node_line
    	

