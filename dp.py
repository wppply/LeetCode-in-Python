# dp

# 
"""
problem 1:
finbonacci: 
there is n steps, for each steps you cna jump 1 or 2.
figure out how many ways are there to jump to the top.
"""

# def jump_top_dp(n):
# 	# tme in O(n)
# 	assert(n>2)
# 	a = [0] * (n+1)
# 	a[1], a[2] = 1, 1

# 	for i in range(3, n+1): 
# 		a[i] = a[i-1] + a[i-2]

# 	return a[n]

# def jump_top_recursion(n): 
# 	# time(2^n)
# 	if n in (1, 2) : return 1 
# 	return jump_top_recursion(n-1) + jump_top_recursion(n-2)

# print(jump_top_dp(20) == jump_top_recursion(20))


"""
problem 2: 
maxmum increase 
gven an array, find a sub array that has all the elements in ascending order
output the length
"""

# def max_ascending_arr_dp(arr): 
# 	n = len(arr)
# 	if n < 1: return None
# 	a = [0] * n # a[i] represent the lon of longest sub-arr ending at i 
# 	a[0] = 1 
# 	for i in range(1, n): 
# 		a[i] = a[i-1] + 1 if arr[i] > arr[i-1] else 1

# 	return max(a)
# print(max_ascending_arr_dp([9,1,2,3,1,2]))

"""
problem 3: \
 jump game\
 given an array arr, arr[i] represents the longest distance you can jump from it\
 figure out whether we can reach the last element if starting at the first one
"""


# def jump_game(arr):
#     n = len(arr)
#     m = [False] * n  # m[i] represents is it posible to reach the end from i
#
#     m[n - 1] = True
#     for i in range(n - 2, -1, -1):
#         d = arr[i]
#         for j in range(i, min(i + d + 1, n)):
#             if m[j] == True:
#                 m[i] = True
#                 break
#     return m
#
# print(jump_game([0, 2, 0, 1]))

"""
Quiz problem
largest subarray
"""


def maxSubarr(arr):
    if not arr: return None
    m = arr[0]
    left, right = 0, 0

    max_cur = arr[0]
    left_cur, right_cur = 0, 0
    for i in range(1, len(arr)):
        if max_cur > 0:
            max_cur = max_cur + arr[i]
            right_cur = i
        else:
            max_cur = arr[i]
            left_cur = i

        if max_cur > m:
            left, right = left_cur, right_cur
            m = max_cur
    return m, left, right


