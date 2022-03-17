class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        #brute force
        #idea: find every pair of three numbers and keep track of their difference from the 
        #   target, return the sum that has the less difference. 
        #implement: 3 nested loop, for each index, loop each remaining indexes with the 
        #   remaining indexes excluding the selected indexes and everyting before. 
        #analysis: since we are doing n^2/2 work for each index, TC: O(n^3)
        #optimal approach
        #idea: instead of finding every single pair of triplets, we can reduce the number of 
        #   pairs we need to generate by sorting the input num array first. with a sorted array,
        #   finding 2 num pair becomes a O(n) operation instead of the O(n^2) operation bc 
        #   we know the min and max of the subarray.
        #implement: sort input arr, loop over all numbers from start to end minus 2, for each
        #   index, we run another loop on the remaining nums with 2 pointers starting at both 
        #   ends of the subarray, checking if the sum of all three numbers have lesser diff 
        #   that what we have so far
        #logic: add all three numbers, check if the diff of absolute value of target and cur sum 
        #   is less than what we have so far. if yes update diff and new sum. update left or 
        #   right depending on whether cur sum is greater or less than target what we have, 
        #   else update both.
        #analysis: TC: O(n^2) bc we are iterating remaining numbers for every index
        #   assuming TC of sorting = O(nlogn). Space: O(1)
        n = len(nums)
        #since we can assume theres always 1 solution, we dont need to check 
        #but good to have 
        if n < 3: return None 
        nums.sort()
        closest_sum = float('inf')
        for i in range(n-2):
            left, right = i+1, n-1
            while left < right:
                cur_sum = nums[i] + nums[left] + nums[right]
                if abs(cur_sum - target) < abs(closest_sum - target): #found
                    closest_sum = cur_sum
                if cur_sum < target:
                    left += 1
                else:
                    right -= 1
        return closest_sum