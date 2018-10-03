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

"""
p1.4: 
unsorted arr, deduplicate for adjacent letters repeatedly
"""

"""
p1.5.1:
given random arr, remove all element to the end of arr 
"""


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



"""
Q4.2
print in zig zag
even: print in order
odd: print in reverse
"""


"""
Q5 
lowest common ancester
"""

"""
Q5.1 
each node pointing to its children only

"""


"""
Q5.2
each has access to parents
"""


"""
Q5.3 
LCA of K nodes
"""


"""
Q5.4
LCA of K-nary tree  
"""


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

