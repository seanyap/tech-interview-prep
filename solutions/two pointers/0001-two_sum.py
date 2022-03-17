class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #bruteforce
        #idea: find every pair of nums and add them up, if their sum is
        #   equal to target, return their indexes
        #algo: run a loop traversing the array of numbers from start to 
        #   end - 1 and in that loop run another loop from start + 1 to
        #   end. for every pair of indexes, check their sum and return if 
        #   they add up to target
        #analysis: 
        #   work done: approx. n^2/2; O(n^2)
        #   memory used: two pointers; O(1)
        #2nd solution
        #idea: sort given array and use two pointers at both ends, check if 
        #   cur sum is equal to target, else check if cur sum is greater or 
        #   lesser than target, then decrease right pointer / increase left 
        #   pointer respectively
        #analysis: TC O(nlogn), SC O(1)
        """
        def twoNumberSum_3(array, targetSum):
            array.sort()
            left = 0
            right = len(array) - 1
            while left < right:
                current_sum = array[left] + array[right]
                if current_sum == targetSum:
                    return [array[left], array[right]]
                elif current_sum < targetSum:
                    right -= 1
                else: #cur sum greater than target 
                    left += 1
            return []
        """
        #optimal solution
        #idea: instead of checking the remaining nums on the RIGHT of the array
        #   with the current num(LOOKING AHEAD for possible values), 
        #   we can check the sum of the current number against PREVIOUSLY seen 
        #   values(num on the LEFT of the array) (LOOKING AT BEHIND/PREVIOUS num 
        #   + memory cache) and see if they add up to target.
        #   Doing this still takes the same number of operations as brute
        #   force. but if we use an aux ds to keep track of prev
        #   nums in memory which allow fast lookup of prev values, 
        #   saving us a lot of repeated access of the same prev value
        #logic: check if we have previously seen a num in the past that add 
        #   our current value to equal to our target num. if yes, we return
        #   the indexes of the prev num & cur num
        #analysis:
        #   work done: n - 1 operations(comparisons). O(n)
        #   memory used: a hashmap of at most size n and 1 pointer. O(n)
        seen_num = dict()
        for i,num in enumerate(nums):
            diff = target - num
            if diff in seen_num:
                #found answer
                return [seen_num[diff], i]
            else:
                #add cur num to hashmap bc it is considered as prev num 
                #for fast lookup for later num
                seen_num[num] = i
        #no valid answer
        return [] 