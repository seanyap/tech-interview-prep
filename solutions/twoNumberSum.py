
# input: an array of distinct positive and negative integers, targetSum 
# output: an array of two numbers which add up to targetSum

# O(n) time | O(n) space
def twoNumberSum(array, targetSum):
    numbers_seen = {}
    for num in array:
        complement = targetSum - num
        if complement in numbers_seen:
            return [num, complement]
        numbers_seen[num] = True
    return []