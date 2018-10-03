def largestRectangleArea(heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    maxx = 0
    left = [0] * len(heights)  # num of histogram larger than i from left
    right = [0] * len(heights)  # num of historgram larger thatn i from right

    for idx in range(1, len(heights)):
        left[idx] = left[idx - 1] + 1 if heights[idx] <= heights[idx - 1] else 0
    for idx in range(len(heights) - 2, -1, -1):
        right[idx] = right[idx + 1] + 1 if heights[idx] <= heights[idx + 1] else 0
    for idx in range(len(heights)):
        s = heights[idx] * (left[idx] + right[idx] + 1)
        maxx = s if maxx < s else maxx
    return maxx

print(largestRectangleArea([2,1,3,4,2,3]))