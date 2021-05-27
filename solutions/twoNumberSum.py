
# input: an array of distinct positive and negative integers, targetSum 
# output: an array of two numbers which add up to targetSum

# 3 solutions with time and space trade off 

# O(n^2) time | O(1)
def twoNumberSum_1(array, targetSum):
    for i in range(len(array) - 1):
        first_num = array[i]
        for j in range(i + 1, len(array)):
            second_num = array[j]
            if first_num + second_num == targetSum:
                return [first_num, second_num]
    return []


# O(n) time | O(n) space
def twoNumberSum_2(array, targetSum):
    numbers_seen = {}
    for num in array:
        complement = targetSum - num
        if complement in numbers_seen:
            return [num, complement]
        numbers_seen[num] = True
    return []


# O(nLog(n)) time | O(1)
def twoNumberSum_3(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        current_sum = array[left] + array[right]
        if current_sum == targetSum:
            return [array[left], array[right]]
        elif current_sum < targetSum:
            left += 1
        elif current_sum > targetSum:
            right -= 1
    return []