"""
p1:
remove repeat element in arr
"""


"""
p1.1:
remove repeat element in sorted arr
"""


def remove_repeat(arr):
    if len(arr) < 2: return arr
    write = 0  # everything before write is the output
    read = 1
    while read < len(arr):
        if arr[read] == arr[write-1]:
            pass  # meet repeat element
        else:
            arr[write] = arr[read]
            write += 1
        read += 1

    return arr[:write]


"""
p1.2:
keep at most 2(or k) elements
"""


def keep_k_element(arr, k):

    if len(arr) <= k: return arr
    read = k + 1
    write = 0
    while write < len(arr):
        if arr[read] != arr[write - 1]:
            arr[write] = arr[read]
            write += 1
        read += 1
    return arr[:write]


"""
p1.3:
keep only unique elements 
"""


def keepUniq(arr):
    if len(arr) < 1:
        return arr
    fast = 0
    slow = 0
    counter = 1
    while fast < len(arr):
        if arr[fast] != arr[slow-1]:
            if counter == 1:
                arr[slow] = arr[fast]
                slow += 1
            counter = 0
        else:
            counter += 1
        fast += 1
    return arr[:slow]

def keepUniq2(arr):
    if len(arr) < 1: return arr
    slow = 1
    fast = 1
    arr = [0] + arr
    while fast < len(arr):
        if arr[fast] != arr[slow-1]:
            arr[slow] = arr[fast]
            fast += 1
            slow += 1
        else:
            slow -= 1  # delete the element on the top
            while fast < len(arr) and arr[fast] == arr[fast-1]:
                fast += 1

        return arr[:slow]

# arr = [1,1,2,3,3,4,5,6,6]
# print("keepUniq:", keepUniq2(arr))

"""
p1.4: 
unsorted arr, deduplicate for adjacent letters repeatedly
"""





"""
p1.5.1:
given random arr, move all 0 to the end of arr 
"""

arr = [1,0,4,3,0,0,1,5,0]


def remove0_1(arr):
    """
    order not kept

    """
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] == 0:
            while right > left and arr[right] == 0:
                right -= 1
            arr[left], arr[right] = arr[right], arr[left]
            right -= 1
            left += 1
        else:
            left += 1
    return arr


def remove0_2(arr):
    slow = 0  # used to output
    fast = 0  # used to search next non-zero element

    while fast < len(arr):
        if arr[slow] == 0:
            # search
            while fast < len(arr) and arr[fast] == 0:
                fast += 1
            if fast >= len(arr): break
            arr[slow], arr[fast] = arr[fast], arr[slow]
        else:
            slow += 1
        fast = max(fast, slow)
    return arr


print("move zero:", remove0_2(arr))




"""
sum:
1. 确定好 slow fast 指针意义！
2. 什么时候更新 slow
3. slow/fast 实际在模拟 stack
4. 同向 相对顺序不变
"""

"""
2D array print problem
剥洋葱
"""


"""
Q3.1 
how to print 2d arr in spiral
"""
def printSpiral(arr):


"""
Q3.2 
Rotate arr 90 degree
"""

"""
BFS
"""


"""
Q4.1 
print binary tree by level 
"""


def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    cur_level = [root]
    res = []
    while cur_level:
        new_level = []
        for node in cur_level:
            if node.left: new_level.append(node.left)
            if node.right: new_level.append(node.right)
        res.append([node.val for node in cur_level if node != None])
        cur_level = new_level
    return res

"""
Q4.2
print in zig zag
even: print in order
odd: print in reverse
"""



def levelOrder(root):
    """
    :type root: TreeNode
    :rtype: List[List[int]]
    """
    cur_level = [root]
    res = []
    flag = -1
    while cur_level:
        new_level = []
        for node in cur_level:
            if node.left: new_level.append(node.left)
            if node.right: new_level.append(node.right)
        res.append([node.val for node in cur_level if node != None][::-1*flag])
        cur_level = new_level
    return res


"""
Q5 
lowest common ancester
"""

"""
Q5.1 
each node pointing to its children only

"""

def LCA(root, node1, node2):

    # base cases
    if root == None: return None
    if root == node1: return node1
    if root == node2: return node2

    left = LCA(root.left, node1, node2)
    right= LCA(root.right, node1, node2)

    if left and right:
        return root

    return left or right


"""
Q5.2
each has access to parents
"""
def LCA_parents(root, node1, node2):
    d1 = depth(root, node1)
    d2 = depth(root, node2)
    if d1 < d2: node1, node2 = node2, node1

    for _ in range(abs(d1-d2)):
        node1 = node1.parents
    for _ in range(min(d1, d2)):
        node1 = node1.parents
        node2 = node2.parents

    if node1 == node2:
        return node1
    else:
        return None



def depth(root, node):
    d = 0
    while node != root:
        d += 1
        node = node.parent
    return d


"""
Q5.3 
LCA of K nodes
"""


def LCA_k(root, node1, node2):

    # base cases
    if root == None: return None
    if root == node1: return node1
    if root == node2: return node2

    left = LCA_k(root.left, node1, node2)
    right= LCA_k(root.right, node1, node2)

    if left and right:
        return root

    return left or right


"""
Q5.4
LCA of K-nary tree  
"""


def LCA_kary(root, node1, node2,k):

    # base cases
    if root == None: return None
    if root == node1: return node1
    if root == node2: return node2

    count = 0
    for ith in range(k):
        if LCA_kary(root.i, node1, node2,k):
            count += 1

    if count > 1:
        return root

    return 1

"""
Q5.5
LCA of K-nary tree for k nodes
"""




"""
Q5.6
search in 100 Machine with map reduce
"""


"""
Q5.7
in BST
"""

def LCA_BST(root, node1, node2):
    # base case
    if not root:
        return None
    if root == node1: return node1
    if root == node2: return node2
    left = LCA_BST(root.left, node1, node2)
    right = LCA_BST(root.right, node1, node2)
    if left or right:
        return left or right

    if min(node1.val, node2.val) < root.val < max(node1.val, node2.val):
        return root
    return None

def lowestCommonAncestor(self, root, p, q):
    """
    :type root: TreeNode
    :type p: TreeNode
    :type q: TreeNode
    :rtype: TreeNode
    """
    if not root: return None

    if root.val > max(p.val, q.val):
        return self.lowestCommonAncestor(root.left, p, q)
    elif root.val < min(p.val, q.val):
        return self.lowestCommonAncestor(root.right, p, q)
    else:
        return root
