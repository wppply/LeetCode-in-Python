# def leftShift(s, idx):
#     left = s[idx:]
#     right = s[:idx]
#     return left+right
#
# print(leftShift("abcd", -1))


# Complete the counts function below.
def counts(nums, maxes):
    nums.sort()  # nlogn
    res = []
    for upbound in maxes:
        c = bs(nums, upbound)
        res.append(c)
    return res


def bs(nums, upbound):
    l, r = 0, len(nums)-1

    while l <= r:
        mid = l + (r-l)//2

        if nums[mid] == upbound:
            return mid + 1
        elif nums[mid] < upbound:
            l = mid + 1
        else:
            r = mid - 1
    return l


print(counts([1,2,3,3,24,25,44,55], [0,24,100]))

