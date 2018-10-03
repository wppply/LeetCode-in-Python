# given string s find all unique substr with k length in order
# import heapq
#
# def getRes(s, l):
# 	h = []
# 	for i in range(l, len(s)): # n
# 		if s[i-l:i] not in h: # n
# 			heapq.heappush(h, s[i-l:i])
# 	return h
#
#
# print(getRes('caaab', 2))
# # print('hello world')

# def reverse(expression):
#     # arr = list(expression[::-1])
#     expression = expression[::-1]
#     res = []
#     stack = []
#     for idx in range(len(expression)):
#         if expression[idx] not in ['*', '/', '+', '-']:
#             stack.append(expression[idx])
#         else:
#             if expression[idx] == "-" and \
#             (idx == len(expression) - 1 or (idx + 1 < len(expression) and expression[idx + 1] in ['*', '/', '+', '-'])):
#                 stack.append(expression[idx])
#             else:
#                 while stack:
#                     res.append(stack.pop())
#                 res.append(expression[idx])
#
#     while stack:
#         res.append(stack.pop())
#
#     return ''.join(res)
# def reverse(expression):
#     arr = list(expression)
#     r
# def reverse(expression):
#     res =[]
#     j = 0
#     for i in range(len(expression)):
#         if expression[i] in ['*', '/', '+', '-']:
#             res.append(expression[j:i])
#             j = i + 1
#             res.append(expression[i])
#     res.append(expression[j:])
#     return ''.join(res[::-1])
# print(reverse("-1*2+9-23"))


# def playlist(songs):
#     d = {}
#     count = 0
#     for i in songs:
#         if i%60 in d:
#             count += d[i%60]
#         elif i%60 == 0 and 60 in d:
#             count += d[60]
#
#         if (60-i%60) in d:
#             d[60-i%60] += 1
#         else:
#             d[60-i%60] = 1
#     return count
# print(playlist([60]*3))

a = list("123456789")
def reverse(arr, i, j):
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

def reverseExp(arr):
    if len(arr) < 2:
        return arr

    arr = list(arr)
    i, j = 0, 1
    while j < len(arr):
        if arr[j] in ['+','-','*','/']:
            reverse(arr, i, j-1)
            i = j + 1
        j += 1
    return ''.join(arr)

print(reverseExp("12-8--9*3"))